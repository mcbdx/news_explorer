"""
    Module to Scrape News Webpages
    Get the following from them:
        - Main title
        - Location 
        - actions
        - import keywords
        - date
        - subjects
"""

### JUST EXPERIMENTING

# libraries
import requests
from bs4 import BeautifulSoup


#  Getter
URL = "https://diario.mx/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

news = []
articles = soup.find_all("article")
for a in articles:
    if a.find("a",class_="rcm12 padding_0",href=True) is not None:
        url = a.find("a",class_="rcm12 padding_0",href=True)['href']
    title = a.find("h2").text
    news.append((title,url))

# get article info
article_url = news[0][1]
article_page = requests.get(article_url)
article_soup = BeautifulSoup(article_page.content, "html.parser")
r =article_soup.find("div",class_="rcm10 padding_0 separacion_grande")
print(r.find("h1").text)
print(r.find("small").text)
print(r.find("p",class_="texto_4").text)


    #print(a.find("h2",class_="titulo_3"))

