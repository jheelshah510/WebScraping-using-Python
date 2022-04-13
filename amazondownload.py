import requests 

x = requests.get("https://www.amazon.in/PS4-Last-Us-Part-II/dp/B07YQ8JMSH/")


fname = "test.html"

with open(fname, "w", encoding="utf-8") as f:
    f.write(x.text)