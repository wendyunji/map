#셀레니움 관련 라이브러리
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

#selenium 기본


#버튼 클릭 이벤트(조회)


#시간 딜레이


#크롤링 
response = requests.get("https://marine.kma.go.kr/custom/security.pop?marineNum=183&type=SECU1")
html = response.text #불러온 response를 text로 변환하여 html 변수에 넣습니다
soup = BeautifulSoup(html,"html.parser")
                                      
#전체 html 중 class 이름이 tbl인 table 찾아서 temps에 저장                                      
temps = soup.find('table',"tbl")
print( temps.get_text() ) #태그 없이 안의 내용만 보고 싶을 떄


table00 = pd.read_html('https://marine.kma.go.kr/custom/security.pop?marineNum=183&type=SECU1')
df00 = pd.Dataframe(table00[0])
print(df)
