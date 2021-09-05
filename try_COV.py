# 메르스 자료 상관관계 분석하기 

import pandas as pd
import numpy as np
import requests
import csv
from bs4 import BeautifulSoup as bs

path = 'C:\Users\idf20\OneDrive\바탕 화면\COVID_MERS-main'
data_csv = pd.read_csv(path + 'DATA_SSC_CORONA_MERS.csv')

df = pd.DataFrame(data_csv)
df

df.info()

# 파일 크기
import os
print("파일 크기 : ")
for file in os.listdir(path):
  if 'csv' in file:
    print(file.ljust(30) + str(round(os.path.getsize(path + file) / 1000000,4)) + "MB")

# 전체 학습 데이터 개수
print("전체 학습 데이터 개수 : {}".format(len(df)))

# 소비업종 종류
consumption_category = set(df['소비업종'])
print('종류 :',consumption_category)
print('갯수 :',len(consumption_category))

# 연령대
age_category = sorted(set(df['연령대']))
print('연령대 :',age_category)
print('범위 :',len(age_category))

# 연도별 정리하기 
date_info = df.소비일자.values
type(date_info)



date_infomation = [str(row) for row in date_info]
type(date_infomation[5])
df['소비일자'] = date_infomation

df['월별'] = pd.to_numeric(df['소비일자'].str[5])
df['연도'] = pd.to_numeric(df['소비일자'].str[0:4])

df.dtypes

year_category = sorted(set(df['연도']))
print('연도 :',year_category)
print('연도 범위 :',len(year_category))

MERS = [] 
COVID = []
columns=['소비업종','성별','연령대','소비건수합계','월별','연도']

for row in df.values:
   if row[6] == 2015:
     MERS.append(row[1:])
   elif row[6] == 2019 or 2020:
     COVID.append(row[1:])
 
MERS = pd.DataFrame(MERS, columns=columns)
COVID = pd.DataFrame(COVID, columns=columns)

print('메르스 자료 개수 :', len(MERS))
print('코로나 자료 개수 :', len(COVID))

print(consumption_m[0]) # 편의점
print(le.classes_)


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

le = LabelEncoder()
tf = StandardScaler()

# 숫자
year_m = MERS['연도']
month_m = MERS['월별']

# 표준화
count_m = MERS['소비건수합계'] 
count_m = np.array(count_m)
count_m = count_m.reshape(-1,1)
count_m = tf.fit_transform(count_m)

# 라벨인코딩 (ML 사용을 위해)
sex_m = le.fit_transform(MERS['성별']) 
ages_m = le.fit_transform(MERS['연령대'])
consumption_m = le.fit_transform(MERS['소비업종'])

# 범주형 변수 상관분석 (성별, 소비업종) , 카이제곱 검정
from scipy.stats import chi2_contingency
print(pd.crosstab(df['성별'], df['소비업종'], margins=True))

sex_com = pd.crosstab(df['성별'], df['소비업종'], margins=False)

# 교차분석 결과값들 일괄계산
# correction = True를 적용하면 Yates'correction이 적용 되어 검정통계량이 보수적으로 더 낮게 나옴
result1 = chi2_contingency(observed=sex_com, correction=False)
print("1. 카이제곱 통계량:", result1[0])
print("2. p-value:", result1[1])
print('3. df:', result1[2]) # (행의개수-1) * (열의 개수 -1)
print('4. 기대값 행렬:', result1[3])

# 범주형 변수 상관분석 (성별, 연령)
pd.crosstab(MERS['성별'], MERS['연령대'], margins=True)

# 상관분석 뭔가 잘못한 듯 하다.
# 이론적으로 개념이 잘못 이해한 듯 하다.
# 조건부를 활용한 데이터 프레임을 추출해 봐야겠다.
# goupby 명령어를 알게 되었다.