import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count
import xml.etree.ElementTree as ET

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


def HollysAddress(result):
    for page_idx in range(0, 56):
        Hollys_URL = 'http://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%s&sido=&gugun=&store=' % str(page_idx + 1)
        print(Hollys_URL)
        response = urllib.request.urlopen(Hollys_URL)
        soupData = BeautifulSoup(response, 'html.parser')
        tbody_tag = soupData.find('tbody')
        for store_tr in tbody_tag.findAll('tr'):
            tr_tag = list(store_tr.strings)
            print(tr_tag)
            if tr_tag[0]!='\n':
                continue
            store_name = tr_tag[4]

            store_sido_gu = tr_tag[2].split()
            store_address = tr_tag[8]


            result.append([store_name]+  store_sido_gu[:2])

    return


def cswin_Hollys():
    result = []

    print('Hollys ADDRESS CRAWLING START')
    HollysAddress(result)
    print(result)
    #hollys_table = pd.DataFrame(result, columns=('store', 'sido', 'store_address'))
    hollys_table = pd.DataFrame(result, columns=('store', 'sido','gungu'))
    hollys_table.to_csv("./hollys2.csv", encoding="cp949", mode='w', index=True)
    del result[:]
    print('FINISHED')


if __name__ == '__main__':
    cswin_Hollys()
