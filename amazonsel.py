import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.by import By
options = Options()
options.headless = False
driver = webdriver.Firefox(options = options)


driver.get("https://www.amazon.in/PS4-Last-Us-Part-II/dp/B07YQ8JMSH/")
time.sleep(5)
price = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[11]/div[1]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]")
print(price.get_attribute('innerHTML'))



f = open("product.html","w",encoding="utf-8")
f.write(driver.page_source)