#! /usr/bin/python3
# coding = utf-8

from bs4 import BeautifulSoup
import requests

url = "https://www.shiyanlou.com/courses/"

doc = requests.get(url)
soup = BeautifulSoup(doc.text)
url_list = [div.img["src"] for div in soup.find_all("div", class_ = "course-cover relative")]
for url in url_list:
    img = requests.get(url)
    with open("pics/" + url.split('/')[-1], 'wb') as f:
        f.write(img.content)
        pass
    pass


