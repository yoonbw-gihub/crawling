import pandas as pd
import numpy as np
LOC=['서울','경기','광주','대구','대전','부산','울산','인천','강원','경상남','경상북','전라남',
            '전라북','충청남','충청북','제주','세종']

print('input mode(anything or short) :')
inp=input()
mode=""
if(inp=='short') :
    print('최소화 모드 실행')
    mode='_short'
else:
    mode=""



mydata= pd.read_csv('./csv/loc'+mode+'.csv', encoding='CP949')
mylist = list(mydata['big'])
allloc=mylist
filename_all=['caffe_pascucci','caffebene','tomandtoms','starbucks','hollys','twosome','yogerpresso','ediya']
additional="_short"
statistics=[]
def csv_chg(name) :
    df = pd.read_csv('./csv/' + name + '.csv', encoding='CP949')
    print('start')
    chgloc = [['경상남도', '경상북도', '전라남도', '전라북도', '충청남도', '충청북도'],
              ['경남', '경북', '전남', '전북', '충남', '충북']]
    for i in range(len(chgloc[0])) :
        df.loc[df.sido==chgloc[0][i],'sido']=chgloc[1][i]
    print(df)
    df.to_csv("./csv/"+name+".csv", encoding="cp949", mode='w', index=True)


def csv_div(name) :
    df = pd.read_csv('./csv/' + name + '.csv', encoding='CP949')
    print(len(df))
    sum = 0
    stt=[]
    #stt.append(name)
    for loc in allloc:
        if '세종특별' in loc :
            num = len(df[df['sido'].str.contains('세종')])
        else :
            sidogun=loc.split()
            #print(sidogun)
            num = len(df[(df['sido'].str.contains(sidogun[0]))&df['gungu'].str.contains(sidogun[1])])
        stt.append(num)
        #print(loc + " : " + str(num))
        sum += num
    statistics.append(stt)


for name in filename_all :
    csv_div(name+additional)

df = pd.read_csv('./csv/' + 'popkorea_short'+mode + '.csv', encoding='CP949')
print()
statistics.append(list(df['income']))
statistics.append(list(df['pop']))
print(statistics)
statistics_table = pd.DataFrame(np.transpose(statistics),
                                columns=['caffe_pascucci','caffebene','tomandtoms','starbucks','hollys','twosome',
                                         'yogerpresso','ediya','pop','income'])
statistics_table.to_csv("./csv/stastic"+mode+".csv", encoding="cp949", mode='w', index=True)
print(statistics_table)
""""""