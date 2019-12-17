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


def YogerpressoAddress(result):
    for page_idx in range(0, 133):
        Yogerpresso_URL = 'https://www.yogerpresso.co.kr/story/search?page=%s&areacode=&s_seq=&s_sido=&s_gugun=&query=' % str(page_idx + 1)
        print(Yogerpresso_URL)
        response = urllib.request.urlopen(Yogerpresso_URL)
        soupData = BeautifulSoup(response, 'html.parser')
        tbody_tag = soupData.find('tbody')
        for store_tr in tbody_tag.findAll('tr'):
            tr_tag = list(store_tr.strings)
            print(tr_tag)
            if tr_tag[0]!='\n':
                continue
            store_name = tr_tag[1]

            #store_sido_gu = tr_tag[4]
            store_address = tr_tag[3].split()


            #result.append([store_name] + [store_address[0]+' '+store_address[1]])
            result.append([store_name] + store_address[:2])

    return


def cswin_Yogerpresso():
    result = []

    print('CHEOGAJIP ADDRESS CRAWLING START')
    YogerpressoAddress(result)
    print(result)
    yogerpresso_table = pd.DataFrame(result, columns=('store', 'sido','gungu'))
    yogerpresso_table.to_csv("./yogerpresso2.csv", encoding="cp949", mode='w', index=True)
    del result[:]
    print('FINISHED')


if __name__ == '__main__':
    cswin_Yogerpresso()
