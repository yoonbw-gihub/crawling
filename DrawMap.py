import pandas as pd
import numpy as np

import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
splt=0

def drawMap(targetData, blockedMap, d1, d2, cmapname):
    whitelabelmin = (max(blockedMap[targetData]) - min(blockedMap[targetData])) * 0.25 + min(blockedMap[targetData])

    datalabel = targetData

    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])

    BORDER_LINES = [
        [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)],  # 서울
        [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)],  # 부산시
        [(14, 8), (16, 8), (16, 10), (15, 10),
         (15, 11), (14, 11), (14, 12), (13, 12)],  # 대구시
        [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)],  # 인천
        [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)],  # 광주시
        [(14, 4), (15, 4), (15, 6)],  # 대전시
        [(15, 11), (16, 11), (16, 13)],  # 울산시
        [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
         (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)],  # 경기도
        [(9, 12), (9, 10), (8, 10)],  # 강원도
        [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
         (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)],  # 충청북도
        [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
         (13, 4), (14, 4), (14, 2)],  # 충청남도
        [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)],  # 전라북도
        [(18, 5), (20, 5), (20, 6)],  # 전라남도
        [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)],  # 경상북도
    ]

    mapdata = blockedMap.pivot(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

    plt.figure(figsize=(8, 13))
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor='#aaaaaa', linewidth=0.5)

    for idx, row in blockedMap.iterrows():
        annocolor = 'white' if row[targetData] > whitelabelmin else 'black'

        if row[d1].endswith('시') and not row[d1].startswith('세종'):
            dispname = '{}\n{}'.format(row[d1][:2], row[d2][:-1])
            if len(row[d2]) <= 2:
                dispname += row[d2][-1]
        else:
            dispname = row[d2][:-1]

        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 9.5, 1.5
        else:
            fontsize, linespacing = 11, 1.2

        plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=2)

    plt.gca().invert_yaxis()
    plt.axis('off')
    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)
    plt.tight_layout()

cafemap = pd.read_csv('./csv/cafe_korea.csv', index_col=0, encoding='ANSI')
tab=['caffe_pascucci','caffebene',	'tomandtoms',	'starbucks',	'hollys',	'twosome',	'yogerpresso','ediya','income','pop']
#   *    drawMap 함수만 인터넷 보고 참고했습니다.
for cafe in tab :
    drawMap(cafe, cafemap, '광역시도', '행정구역', 'Greens')
    plt.savefig('korea_'+cafe+'.png', dpi=300)
