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


def CaffebeneAddress(result):
    for page_idx in range(0, 34):
        Caffebene_URL = 'http://bf.caffebene.co.kr/Content/Gnb/Store/Map.aspx?code=T5M2I2&SearchValue=&gugun=&StoreName=&room=N&wifi=N&all=N&pc=N&book=N&store=N&Page=%s' % str(page_idx + 1)
        print(Caffebene_URL)
        response = urllib.request.urlopen(Caffebene_URL)
        soupData = BeautifulSoup(response, 'html.parser')
        tbody_tag = soupData.find('div', attrs={'class': 'listWrap type05'})

        for store_tr in tbody_tag.findAll('li'):
            tr_tag = list(store_tr.strings)
            print(tr_tag)
            store_name = tr_tag[2]
            store_address = tr_tag[4]
            store_sido_gu = store_address.split()[:2]
            #result.append([store_name] + store_sido_gu + [store_address])
            result.append([store_name] + store_sido_gu)

    return


def cswin_Caffebene():
    result = []

    print('Caffebene ADDRESS CRAWLING START')
    CaffebeneAddress(result)
    print(result)
    #cheogajip_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    Caffebene_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu'))
    Caffebene_table.to_csv("./caffebene2.csv", encoding="cp949", mode='w', index=True)
    del result[:]
    print('FINISHED')


if __name__ == '__main__':
    cswin_Caffebene()
