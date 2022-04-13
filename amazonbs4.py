from bs4 import BeautifulSoup
import requests 

f = open("product.html","r",encoding="utf-8")
content = f.read()
soup = BeautifulSoup(content,"html.parser")

print(soup.find(class_="a-offscreen").get_text())