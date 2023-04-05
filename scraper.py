import requests
from bs4 import BeautifulSoup

#product_code=input("Podaj kod produktu: ")

product_code="96693065"
url=f"https://www.ceneo.pl/{product_code}#tab=reviews"
response=requests.get(url)
page_dom=BeautifulSoup(response.text,"html.parser")
opinions=page_dom.select("div.js_product-review")
all_opinions=[]

for opinion in opinions:
    single_opinion={
        "opinion_id":opinion["data-entry-id"],
        "author":opinion.select_one("span.user-post__author-name").text.strip(),
        "recomendation":opinion.select_one("span.user-post__author-recomedation>em").text.strip(),
        "rating":opinion.select_one("span.user-post__score-count").text.strip(),
        "verified":opinion.select_one("div.review-pz").text.strip(),
        "post_date":opinion.select_one("span.user-post_published>time:nth-child(1)[")["datatime"].strip(),
        "purchase_date":opinion.select_one("span.user-post_published>time:nth-child(2)[")["datatime"].strip(),
        "vote_up":opinion.select_one("").text.strip(),
        "vote_down":opinion.select_one("").text.strip(),
        "content":opinion.select_one("").text.strip(),
        "cons":opinion.select_one("").text.strip(),
        "pros":opinion.select_one("").text.strip(),
    }
    print(type(opinion))
