import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
from itertools import count
from selenium import webdriver

import ssl  # 추가


def get_request_url(url, enc='utf-8'):
    req = urllib.request.Request(url)
    try:
        ssl._create_default_https_context = ssl._create_unverified_context  # 추가
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')

            return ret
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
def EdiyaAddress(result):
    Ediya_URL = 'https://www.ediya.com/contents/find_store.html#c'
    wd = webdriver.Chrome('./chromedriver.exe')
    wd.get(Ediya_URL)
    time.sleep(5)

    mydata= pd.read_csv('./csv/test3.csv', encoding='CP949')
    mylist = list(mydata['big'])

    for city in mylist :
        print("inpjut")
        path = '//*[@id="contentWrap"]/div[3]/div/div[1]/ul/li[2]/a'

        wd.find_element_by_xpath(path).click()
        time.sleep(2)
        wd.find_element_by_id('keyword').send_keys(city)
        path = '// *[ @ id = "keyword_div"] / form / button'
        wd.find_element_by_xpath(path).click()
        time.sleep(2)
        for page_idx in range(1):
            time.sleep(2)


            try :
                rcv_data = wd.page_source
                soupData = BeautifulSoup(rcv_data, 'html.parser')
                #print(soupData)
                tbody_tag = soupData.find('div', attrs={'class': 'result_list'})
                #print(tbody_tag)
                for store_list in tbody_tag.findAll('dl'):
                    print(store_list)
                    tr_tag = list(store_list.strings)
                    print(tr_tag)
                    if (tr_tag[0] == '등록된 데이터가 없습니다.'):
                        return result
                    store_name = tr_tag[0]
                    store_address = tr_tag[2]
                    store_sido_gu = store_address.split()[:2]
                    result.append([store_name] + store_sido_gu)
            except :
                print("결과없음.")
    return
def cswin_Ediya():
    result = []

    print('Ediya ADDRESS CRAWLING START')
    EdiyaAddress(result)
    Ediya_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu'))
    Ediya_table.to_csv("./csv/ediya2.csv", encoding="cp949", mode='w', index=True)

    print('FINISHED')

if __name__ == '__main__':
    cswin_Ediya()
