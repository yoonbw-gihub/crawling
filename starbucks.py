from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

chromedriver_dir = 'chromedriver.exe'
wd = webdriver.Chrome(chromedriver_dir)
wd.get('https://www.istarbucks.co.kr/store/store_map.do')


def loc_find(idx):
    try:
        wd.find_element_by_class_name('loca_search').click()
        time.sleep(1)
        wd.find_element_by_class_name('sido_arae_box').find_elements_by_tag_name('li')[idx].click()
        time.sleep(1)
        wd.find_element_by_class_name('gugun_arae_box').find_element_by_tag_name('li').click()
        if idx==0:
            time.sleep(3)
        else :
            time.sleep(1)
    except:
        print("")
address = []
time.sleep(5)
for i in range(17):
    loc_find(i)
    source = wd.page_source
    soupData = BeautifulSoup(source, 'html.parser')
    soupData = soupData.find('ul', class_='quickSearchResultBoxSidoGugun')  # 주소
    li_list = soupData.find_all('li')


    for info in li_list:
        sido = info.find('p').text.split()[:2]
        print((info.find('strong').text))
        address.append([info.find('strong').text] + sido)
    time.sleep(3)
df = pd.DataFrame(address, columns = ['store','sido','gungu'])
print(df)
df.to_csv("./starbucks_final.csv", encoding="cp949", mode='w', index=True)