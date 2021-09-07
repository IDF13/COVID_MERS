# DATA_SSC_CORONA_MERS.csv 파일 데이터 분석 연습
# --------------------------------------------------------------------

import pandas as pd
import numpy as np
import requests
import csv
from bs4 import BeautifulSoup as bs

path = '/content/drive/MyDrive/ML Deep/'
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

# 데이터 정보를 텍스트로 받았을 경우 데이터 타입 확인
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
le.classes_
