import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
from itertools import count
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import ssl  #추가

def get_request_url(url, enc='utf-8'):

    req = urllib.request.Request(url)


    try:
        ssl._create_default_https_context = ssl._create_unverified_context    #추가

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
def dellist(big) :
    new=[]
    for small in big :
        if small!="""\n""" :
            new.append(small)
    return new
def twosomeAddress(result):
    twosome_URL = 'https://www.twosome.co.kr:7009/store/list.asp'
    wd = webdriver.Chrome('./chromedriver.exe')
    wd.get(twosome_URL)
    time.sleep(5)
    select1=[ '대전','전라','광주','경기','세종','인천','경상','강원'  ,'울산' ,'전북' ,'제주','경남','충북' ,'전남'  ,'부산'
            ,'대구' ,'충남' ,'경북', '서울']
    for i in select1 :
        select = Select(wd.find_element_by_id('area'))
        select.select_by_value(i)
        time.sleep(1)
        rcv_data = wd.page_source
        soupData = BeautifulSoup(rcv_data, 'html.parser')
        mst = soupData.find('select', attrs={'id': 'area2'})
        select2 = list(mst.strings)
        if i!='세종' :
            select2.remove("구/군")
            select2 = dellist(select2)

        for k in select2 :
            if i != '세종':
                select = Select(wd.find_element_by_id('area2'))
                select.select_by_value(k)
            wd.execute_script("search();")
            time.sleep(2)

            for page_idx in range(120):
                txt="xmlList('','%s','P','%s','%s','');" % (str(page_idx + 1), i,k)
                print(txt)
                wd.execute_script("xmlList('','%s','P','%s','%s','');" % (str(page_idx + 1), i,k))
                print("PageIndex [%s] Called" % (str(page_idx + 1)))
                time.sleep(2)

                rcv_data = wd.page_source
                soupData = BeautifulSoup(rcv_data, 'html.parser')
                mst = soupData.find('table', attrs={'class': 'mt30 tbl-list02'})
                mst = mst.find('tbody')
                j = 0
                for store_list in mst.findAll('tr'):
                    # print(store_list)

                    myaddr = list(store_list.strings)
                    print(myaddr)
                    if myaddr[0] == '+++ 검색된 매장이 없습니다 +++':
                        break
                    print(myaddr[3].strip())
                    result.append([myaddr[3].strip()] + [i]+[k])
                    j = j + 1
                if j != 10:
                    break

    return

def cswin_twosome ():

    result = []

    print('twosome ADDRESS CRAWLING START')
    twosomeAddress(result)
    print(result)
    twosome_table = pd.DataFrame(result, columns=('store','sido','gungu'))
    twosome_table.to_csv("./2some4.csv", encoding="cp949", mode='w', index=True)

    print('FINISHED')


if __name__ == '__main__':
     cswin_twosome ()
