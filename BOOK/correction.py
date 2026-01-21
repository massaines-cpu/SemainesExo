import json
from bs4 import BeautifulSoup
import requests
html = requests.get('https://books.toscrape.com/index.html')

soup = BeautifulSoup(html.text, 'html.parser')

# POUR CHAQUE PAGE
ol = soup.select('ol.row') #toute la page
li_s = ol[0].select("li")
bib = []
for li in li_s:
    livre = {}
    livre["titre"] = li.select('h3')[0].select('a')[0]['title']
    href = li.select('h3')[0].select('a')[0]['href']
    adresse_total = "https://books.toscrape.com/"+href
    soup_livre = BeautifulSoup(requests.get(adresse_total).text, 'html.parser')
    livre["description"] = soup_livre.select(".product_page > p:nth-child(3)")[0].text
    livre["prix"] = float(li.select('p.price_color')[0].text.replace("Â£", ""))
    # livre['category'] = soup_livre.select('div.page-header.action')[0].text
    bib.append(livre)

next_page = soup.select('li.next > a')

print(bib)
print(len(bib))
# with open('bib.json', "w") as f:
#     json.dump(bib, f)

