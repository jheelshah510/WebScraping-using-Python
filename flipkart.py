from bs4 import BeautifulSoup
import requests

#url = "https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29"
url="https://www.flipkart.com/search?q=smartphone"
response = requests.get(url)



soup = BeautifulSoup(response.content,"html.parser")


names=soup.find_all('div',class_="_4rR01T")
prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
for n,p in zip(names,prices):
    print(n.text+"    " +p.text)