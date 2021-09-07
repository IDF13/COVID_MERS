### groupby 함수 사용

import pandas as pd
import numpy as np

path = '/content/drive/MyDrive/ML Deep/'
data_csv = pd.read_csv(path + 'DATA_SSC_CORONA_MERS.csv')

df = pd.DataFrame(data_csv)
df.head()

# 연도별 정리하기 
date_info = df.소비일자.values
type(date_info)

date_infomation = [str(row) for row in date_info]
type(date_infomation[5])
df['소비일자'] = date_infomation

df['월별'] = df['소비일자'].str[5]
df['연도'] = df['소비일자'].str[0:4]

df = df.drop(['소비일자'],axis=1)
df

'''
# 판다스 조건부 추출
woman = df['성별'] == '여성'
man = df['성별'] == '남성'
age_20 = df['연령대'] == '20대'
year_2020 = df['연도'] == 2020
year_2019 = df['연도'] == 2019

woman_20_2019 = df[woman & age_20 & year_2019]
man_20_2019 = df[woman & age_20 & year_2019]

woman_20_2020 = df[woman & age_20 & year_2020]
man_20_2020 = df[woman & age_20 & year_2020]

woman_20_2019 = woman_20_2019.drop(['성별','연령대','연도','월별'], axis=1)
woman_20_2020 = woman_20_2020.drop(['성별','연령대','연도','월별'], axis=1)

'''
# woman_20_2019 = df[['성별','연령대','연도']] 와 다르다.

# 1가지 범주 그룹별로 분류
grouped1 = df['소비건수합계'].groupby(df['소비업종'])
grouped2 = df['소비건수합계'].groupby(df['성별'])
grouped3 = df['소비건수합계'].groupby(df['연령대'])
grouped4 = df['소비건수합계'].groupby(df['연도'])
grouped5 = df['소비건수합계'].groupby(df['월별'])

# 2가지 이상 범주 그룹별로 분류 -> 연속형 자료가 자동으로 설정
grouped6 = df.groupby(['소비업종','연령대','성별','연도'])

grouped6.sum().to_csv('/content/drive/MyDrive/ML Deep/group.csv')

grouped6.sum()

for key, group in grouped6:
  print("* key", key)
  print("* count",len(group))
  print(group.head())
  print("\n")

'''
'가전/가구', '요식/유흥', '가정생활/서비스', 
'스포츠/문화/레저', '할인점/마트', '패션/잡화', 
'여행/교통', '교육/학원', '주유', '자동차', 
'편의점', '미용', '의료', '백화점/상품권/아울렛'
'''

grouped6.describe().to_csv('/content/drive/MyDrive/ML Deep/group.csv',encoding='cp949')

grouped6.describe()


# 데이터 프레임을 분류하는 함수를 알아보았다.
# 하지만 시각화 하는데 어려움을 느껴 
# 직접 클래스를 이용해 분류기를 만들어 볼 생각이다.
