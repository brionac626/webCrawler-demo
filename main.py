from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

weatherInfoTW = "https://www.cwb.gov.tw/V8/C/W/OBS_Map.html"

ops = Options()
ops.add_argument("--disable-notifications")

chrome = webdriver.Chrome("./chromedriver.exe", chrome_options=ops)
chrome.get(weatherInfoTW)

soup = BeautifulSoup(chrome.page_source, "html.parser")

citys = soup.select(".city")
tems = soup.select(".tem-C")

i = 0
while i < len(citys):
    print(citys[i].getText(), tems[i].getText())
    i += 1
