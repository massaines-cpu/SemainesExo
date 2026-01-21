import json
from bs4 import BeautifulSoup
import requests

# 1. On prépare la liste qui contiendra tous nos livres
tous_livres = []
url_actuelle = 'https://books.toscrape.com/catalogue/page-1.html'

# On lance une boucle pour gérer les pages (on va en faire 2 pour l'exemple)
for page in range(50):
    print(f"Extraction de la page {page + 1}...")
    html = requests.get(url_actuelle)
    soup = BeautifulSoup(html.text, 'html.parser')

    # On récupère tous les livres de la page
    li_s = soup.select("ol.row li")

    for li in li_s:
        livre = {}

        # INFOS SUR LA PAGE D'ACCUEIL
        livre["titre"] = li.select('h3 a')[0]['title']
        livre["prix"] = float(li.select('p.price_color')[0].text.replace("£", "").replace("Â", ""))

        # ON VA SUR LA PAGE DU LIVRE (pour la description, l'UPC et la catégorie)
        href = li.select('h3 a')[0]['href']
        # Attention au lien : il faut parfois le nettoyer
        adresse_total = "https://books.toscrape.com/catalogue/" + href.replace("catalogue/", "")

        page_livre = requests.get(adresse_total)
        soup_livre = BeautifulSoup(page_livre.text, 'html.parser')

        # La description  4ème paragraphe
        livre["description"] = soup_livre.select("article.product_page p")[3].text
        #livre["description"] = soup_livre.select(".product_page > p:nth-child(3)")[0].text

        # L'UPC (il est caché dans un tableau <table>)
        livre["upc"] = soup_livre.select("table tr td")[0].text

        # La Catégorie (elle est dans le "fil d'ariane" en haut de page)
        livre["categorie"] = soup_livre.select("ul.breadcrumb li a")[2].text
        #livre['categorie'] = soup_livre.select('.page-header.action h1')[0].text

        tous_livres.append(livre)


    next_btn = soup.select('li.next a')
    if next_btn:
        url_actuelle = "https://books.toscrape.com/catalogue/" + next_btn[0]['href']
    else:
        break  # Plus de page suivante, on s'arrête

print(tous_livres)

with open('tous_livres.json', "w") as f:
    json.dump(tous_livres, f)
