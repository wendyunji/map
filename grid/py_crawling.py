import requests as rq
from  bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time


url = "https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")


chrome_driver_path =(r"/home/ubuntu/hanium-seungsoo/map/grid/chromedriver")
driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
driver.get(url)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#tbl = soup.find('table','tbl')
#print(tbl.get_text())
#print(type(tbl))

table00 = pd.read_html(url)
df00 = pd.DataFrame(table00[0])
print(df00)
df00.to_csv('df/df00.csv', encoding='utf-8')


#버튼 클릭 이벤트(03시 조회)
hbutton = driver.find_element_by_link_text("h003")
print(hbutton)
hbutton.click()

searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button")
print(searchbutton)
searchbutton.click()
tbl = soup.find('table','tbl')
tb_text = tbl.get_text()
print(tb_text)
print(type(tb_text))

df03 = pd.DataFrame([x.split('\n') for x in tb_text.split('\n\n')])
print(df03[0:6].head(2)) 



#table03 = pd.read_html(url)
#df03 = pd.DataFrame(table03[0])
#print(df03)
#df03.to_csv('df/df03.csv', encoding='utf-8')

