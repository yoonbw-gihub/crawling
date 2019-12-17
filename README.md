# 데이터 크롤링 기말과제

## 제출파일

- Readme.md : Readme 
- 2013301046_윤병욱.ppt : 제출할 프레젠테이션 파일.

- 2some2.py : 투썸플레이스의 홈페이지에서 매장이름, 매장주소를 크롤링하는 파이썬파일.
- caffe hollys.py : 할리스 커피의 홈페이지에서 매장이름, 매장주소를 크롤링하는 파이썬파일.
- caffe pascucci.py : 카페 파스꾸찌의 홈페이지에서 매장이름, 매장주소를 크롤링하는 파이썬파일.
- caffebenei.py : 카페베네의 홈페이지에서 매장이름, 매장주소를 크롤링하는 파이썬파일.
- DrawMap.py : '/csv/cafe_korea.csv를 보고 지도모양의 그래프를 만들어주는 파이썬파일.
- ediya_caffe.py : 이디야 커피의 홈페이지에서 매장이름, 매장주소를 크롤링하는 파이썬파일.
- paikdabang.py : 빽다방의 홈페이지에서 매장이름, 매장주소를 크롤링하는 파이썬파일.
- refine&result.py : csv파일을 시/도의 이름을 통일시켜주도록 refine하는 기능과
                    카페 프랜차이즈에서 크롤링한 모든 csv파일과 시군구별 소득,인구수 csv파일을 합쳐주는 파이썬파일.
- starbucks.py : 스타벅스의 홈페이지에서 매장이름, 매장주소를 크롤링하는 파이썬파일.
- t&t.py : 탐앤탐스의 홈페이지에서 매장이름, 매장주소를 크롤링하는 파이썬파일.
- yogerpresso.py : 요거프레스의 홈페이지에서 매장이름, 매장주소를 크롤링하는 파이썬파일.

- MyAnalysis.ipynb : 인구수 기준, 수입 기준, 스타벅스 매장수 기준으로 선형회귀분석을 수행하는 jupyter Notebook 팦일.

- korea_caffe_pascucci.png : 카페 파스꾸찌의 시군구별 분포도를 보여주는 png파일.
- korea_caffebene.png : 카페베네의 시군구별 분포도를 보여주는 png파일.
- korea_ediya.png : 이디야 커피의 시군구별 분포도를 보여주는 png파일.
- korea_hollys.png : 할리스 커피의 시군구별 분포도를 보여주는 png파일.
- korea_pop.png : 인구의 시군구별 분포도를 보여주는 png파일.
- korea_starbucks.png : 스타벅스의 시군구별 분포도를 보여주는 png파일.
- korea_tomandtoms.png : 탐앤탐스의 시군구별 분포도를 보여주는 png파일.
- korea_twosome.png : 투썸플레이스의 시군구별 분포도를 보여주는 png파일.
- korea_yogerpresso.png : 요거프레스의 시군구별 분포도를 보여주는 png파일.

### CSV폴더 내부

- cafe_korea.csv : DrawMap에 쓰이는 한국 시군구별 카페 분포도를 간략하게 모아놓은 것.
- caffe_pascucci_short.csv : 카페파스꾸찌의 크롤링 결과 파일.
- caffebene_short.csv : 카페베네의 크롤링 결과 파일
- ediya_short.csv : 이디야 카페의 크롤링 결과 파일
- hollys_short.csv : 할리스 커피의 크롤링 결과 파일
- loc.csv : 시군구의 모든 이름이 있는 파일
- loc_short.csv : 시군구의 간략한 이름(stastic_short.csv생성을 위해)이 있는 파일
- popkorea_short.csv : 시군구별 인구수와 수입이 있는 파일
- popkorea_short_short.csv : 시군구별 간략한 인구수와 수입이 있는 파일
- starbucks_short.csv : 스타벅스의 크롤링 결과 파일
- stastic.csv : refine&result에서 종합 csv파일 만들때 생성되는 종합파일
- stastic_short.csv : refine&result에서 간략한 종합 csv파일 만들때 생성되는 종합파일
- tomandtoms_short.csv : 탐앤탐스의 크롤링 결과 파일
- twosome_short.csv : 투썸플레이스의 크롤링 결과 파일
- yogerpresso_short.csv : 요거프레스의 크롤링 결과 파일
