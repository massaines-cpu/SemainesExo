import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
ol = soup.select('ol.row')
les_titres = soup.find_all('titre', class_='product_pod')

#upc = th.td class='table table-striped'
#description id=product_description class_='sub-header', div.h2 "pour avoir le titre",
#le contenu est dans p
#categorie = class_='page-header action'
#code pour une page, mais besoin des autres, bouton next
liste_des_livres = []
for article in les_titres:
    titre = article.h3.a['title']
    liste_des_livres.append(titre)
print(liste_des_livres)

# def prix():
#     liste_des_prix = []
#     for price in prices:
#         price_ex = span.h1.p['price_color']
#         liste_des_prix.append(price_ex)
#     print(liste_des_prix)