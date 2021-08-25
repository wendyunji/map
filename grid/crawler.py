import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

Options= webdriver.ChromeOptions()
Options.add_argument('--headless')
Options.add_argument('--no-sandbox')
Options.add_argument("--single-process")
Options.add_argument("--disable-dev-shm-usage")


#selenium 기본
chrome_driver_path =(r"/home/ubuntu/hanium-seungsoo/map/grid/chromedriver")
url2 = 'https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645'
driver = webdriver.Chrome(chrome_driver_path,options=Options)
driver.get('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')

#버튼 클릭 이벤트(조회)
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()

#시간 딜레이


#크롤링 
table00 = pd.read_html('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')
df00 = pd.Dataframe(table00[0])
print(df)

#버튼 클릭 이벤트(03시 조회)
searchbutton = driver.find_element_by_css_selector("#ztree1_4_a > label").click()
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()
table03 = pd.read_html('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')
df03 = pd.Dataframe(table03[0])
print(df03)

#버튼 클릭 이벤트(06시 조회)
searchbutton = driver.find_element_by_css_selector("#ztree1_5_a > label").click()
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()
table06 = pd.read_html('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')
df06 = pd.Dataframe(table06[0])
print(df06)

#버튼 클릭 이벤트(09시 조회)
searchbutton = driver.find_element_by_css_selector("#ztree1_6_a > label").click()
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()
table09 = pd.read_html('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')
df09 = pd.Dataframe(table09[0])
print(df09)


searchbutton = driver.find_element_by_css_selector("#ztree_2_switchl").click()
searchbutton = driver.find_element_by_css_selector("#ztree_4_a > label").click()
searchbutton = driver.find_element_by_css_selector("#ztree1_3_a > label").click()
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()
table1200 = pd.read_html('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')
df1200 = pd.Dataframe(table1200[0])
print(df1200)

searchbutton = driver.find_element_by_css_selector("#ztree_2_switchl").click()
searchbutton = driver.find_element_by_css_selector("#ztree_4_a > label").click()
searchbutton = driver.find_element_by_css_selector("#ztree1_4_a > label").click()
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()
table1203 = pd.read_html('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')
df1203 = pd.Dataframe(table1203[0])
print(df1203)

searchbutton = driver.find_element_by_css_selector("#ztree_2_switchl").click()
searchbutton = driver.find_element_by_css_selector("#ztree_4_a > label").click()
searchbutton = driver.find_element_by_css_selector("#ztree1_5_a > label").click()
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()
table1206 = pd.read_html('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')
df1206 = pd.Dataframe(table1206[0])
print(df1206)

searchbutton = driver.find_element_by_css_selector("#ztree_2_switchl").click()
searchbutton = driver.find_element_by_css_selector("#ztree_4_a > label").click()
searchbutton = driver.find_element_by_css_selector("#ztree1_6_a > label").click()
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()
table1209 = pd.read_html('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')
df1209 = pd.Dataframe(table1209[0])
print(df1209)