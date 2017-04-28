# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup


PROXIES = {
    "http": "http://127.0.0.1:1080",
    "https": "https://127.0.0.1:1080"
}

MTR_NUMBERS = [1, 2, 3, 4, 5, 7, 9, 11]

def save_wiki_content():
    content = requests.get("https://zh.wikipedia.org/zh-cn/%E6%B7%B1%E5%9C%B3%E5%9C%B0%E9%93%81%E8%BD%A6%E7%AB%99%E5%88%97%E8%A1%A8", proxies=PROXIES).content.decode()

    with open("mrt.html", "w", encoding="utf-8") as f:
        f.write(content)


with open("mrt.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")


stations = []
for line_num in MTR_NUMBERS:
    line_id = "{}.E5.8F.B7.E7.B6.AB".format(line_num)
    h3 = soup.find("span", id=line_id).parent
    table = h3.next_sibling.next_sibling

    
