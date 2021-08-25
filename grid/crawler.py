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
print("start")
driver.get('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')
print("end")

#버튼 클릭 이벤트(조회)
searchbutton = driver.find_element_by_css_selector("#dsForm > div.wrap_btn > button").click()

#시간 딜레이


#크롤링 
table00 = pd.read_html('https://data.kma.go.kr/data/mrz/mrzRltmList.do?pgmNo=645')
df00 = pd.Dataframe(table00[0])
print(df)

