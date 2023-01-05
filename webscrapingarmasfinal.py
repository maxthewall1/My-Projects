'''
WEB SCRAPING FROM INSIGHT CRIME USING BEAUTIFULSOUP (all pages focused on get infos about arms trafficking in South America)
'''

import requests
from bs4 import BeautifulSoup

URL = "https://insightcrime.org/page"

print("ARMS TRAFFICKING\n==============================\n")
for page in range(0, 103):
    req = requests.get(URL + str(page) + '/' + '?s=Arms+Trafficking')

    soup = BeautifulSoup(req.content, "html.parser")
    results = soup.find(id="content")




    arms_articles = results.find_all(
        "h2", text=lambda text: 'honduras' in text.lower()
    )

    arms_articles_elements = [
        h2_element.parent for h2_element in arms_articles
    ]

    for arms_element in arms_articles_elements:
        title_element = arms_element.find("h2")

        print(title_element.text.strip())

        link_url = arms_element.find_all("a")[1]["href"]
        print(f"Disponível em: {link_url}\n")
        print()
