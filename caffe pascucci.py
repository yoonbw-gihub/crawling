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


def PascucciAddress(result):
    for page_idx in range(0, 50):
        Pascucci_URL = 'http://www.caffe-pascucci.co.kr/store/storeList.asp?page=%s' % str(page_idx + 1)
        print(Pascucci_URL)
        response = urllib.request.urlopen(Pascucci_URL)
        soupData = BeautifulSoup(response, 'html.parser')
        tbody_tag = soupData.find('tbody')
        for store_tr in tbody_tag.findAll('tr'):
            tr_tag = list(store_tr.strings)
            print(tr_tag)
            if tr_tag[0]!='\n':
                continue
            store_name = tr_tag[3]

            store_sido_gu = tr_tag[5]
            i=6
            while tr_tag[i]=='\n':
                i=i+1
            store_address = tr_tag[i]

            result.append([store_name] + [store_sido_gu] + [store_address.split()[1]])

    return


def cswin_Pascucci():
    result = []

    print('Pascucci ADDRESS CRAWLING START')
    PascucciAddress(result)
    print(result)
    caffe_pascucci_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu'))
    caffe_pascucci_table.to_csv("./caffe_pascucci2.csv", encoding="cp949", mode='w', index=True)
    del result[:]
    print('FINISHED')


if __name__ == '__main__':
    cswin_Pascucci()
