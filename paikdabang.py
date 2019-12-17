import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
from itertools import count
from selenium import webdriver
from selenium.webdriver.common.by import By

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


def PaikAddress(result):
    Paik_URL = 'http://paikdabang.com/store/'
    wd = webdriver.Chrome('./chromedriver.exe')
    wd.get(Paik_URL)
    time.sleep(4)
    for page_idx in range(3):
        path = '//*[@id="pagination"]/li[%s]' % str(page_idx + 2)
        wd.find_element_by_xpath(path).click()
        print(path)

        rcv_data = wd.page_source
        soupData = BeautifulSoup(rcv_data, 'html.parser')
        for store_list in soupData.findAll('tbody', attrs={'id': 'store_list'}):
            print(store_list)
            for store_tr in store_list:
                tr_tag = list(store_tr.strings)
                print(tr_tag)
                if (tr_tag[0] == '등록된 데이터가 없습니다.'):
                    return result
                if(tr_tag[1] == ' '):
                    continue
                store_sido = tr_tag[1]
                store_name = tr_tag[3]
                store_address = tr_tag[5]
                # store_sido_gu = store_address.split()[:2]
                result.append([store_name] + [store_sido] + [store_address])
        time.sleep(2)
    for page_next in range(25) :
        try :
            # wd.execute_script("store.goPage('%s')" % str(page_idx + 1))
            path = '//*[@id="pagination"]/li[6]'
            wd.find_element_by_xpath(path).click()
            print(path)
            rcv_data = wd.page_source
            soupData = BeautifulSoup(rcv_data, 'html.parser')
            for store_list in soupData.findAll('tbody', attrs={'id': 'store_list'}):
                print(store_list)
                for store_tr in store_list:
                    tr_tag = list(store_tr.strings)
                    print(tr_tag)
                    if (tr_tag[0] == '등록된 데이터가 없습니다.'):
                        return result
                    if (tr_tag[1] == ' '):
                        continue
                    store_sido = tr_tag[1]
                    store_name = tr_tag[3]
                    store_address = tr_tag[5]
                    # store_sido_gu = store_address.split()[:2]
                    result.append([store_name] + [store_sido] + [store_address])

            time.sleep(5)
        except :
            return

    return

def cswin_Paik():
    result = []

    print('Paik ADDRESS CRAWLING START')
    PaikAddress(result)
    print(result)
    Paik_table = pd.DataFrame(result, columns=('store', 'sido', 'store_address'))
    Paik_table.to_csv("./Paik.csv", encoding="cp949", mode='w', index=True)

    print('FINISHED')


if __name__ == '__main__':
    cswin_Paik()

