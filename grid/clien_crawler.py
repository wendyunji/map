#셀레니움 관련 라이브러리
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

#selenium 기본
chrome_driver_path = "/Users/seungsoo/Downloads/chromedriver"
url = 'https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645'
browser = webdriver.Chrome(chrome_driver_path)
browser.get(url)

#버튼 클릭 이벤트(조회)
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()

#시간 딜레이
time.sleep(3)

#크롤링 
response = requests.get(url)
html = response.text #불러온 response를 text로 변환하여 html 변수에 넣습니다
soup = BeautifulSoup(html,"html.parser")
                                      
#전체 html 중 class 이름이 tbl인 table 찾아서 temps에 저장                                      
temps = soup.find('table',"tbl")
print( temps.get_text() ) #태그 없이 안의 내용만 보고 싶을 떄




searchbutton = driver.find_element_by_css_selector("#ztree1_4_a > label").click()
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()



searchbutton = driver.find_element_by_css_selector("#ztree1_5_a > label").click()
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()


searchbutton = driver.find_element_by_css_selector("#ztree1_6_a > label").click()
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()
