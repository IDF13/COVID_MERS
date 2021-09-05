import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = '/content/drive/MyDrive/ML Deep/'
COVID_MERSS = pd.read_csv(path + "DATA_SSC_CORONA_MERS.csv")
 
covid_merss = pd.DataFrame(COVID_MERSS)
covid_merss

# 모든 경우의 수를 고려한 변수를 분류하는 클래스 정의 --> 경우의 수가 많아져서 다른 방안 고민
'''
class Classification():
  def __init__(self,name, data):
    self.name = name
    self.data = data
   
    
 
  def split_factor(self,factor_name, sex='전부', age='전연령', year='3년', month='3개월'):
    self.factor_name = factor_name
    self.sex = sex
    self.age = age
    self.year = year
    self.month = month 
  
    if self.sex == '전부':
      self.name = [row for row in self.data.values if row[0] == self.factor_name and row[2] == self.age and row[4] == self.year and row[5] == self.month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])

    elif self.age == '전연령':
      self.name = [row for row in self.data.values if row[0] == self.factor_name and row[1] == self.sex and row[4] == self.year and row[5] == self.month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])

    elif self.year == '3년':
      self.name = [row for row in self.data.values if row[0] == self.factor_name and row[1] == self.sex and row[2] == self.age and row[5] == self.month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])

    elif self.month == '3개월':
      self.name = [row for row in self.data.values if row[0] == self.factor_name and row[1] == self.sex and row[2] == self.age and row[4] == self.year]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])
 
    elif self.sex == '전부' and self.age == '전연령' and self.year == '3년' and self.month == '3개월':
      self.name = [row for row in self.data.values if row[0] == self.factor_name]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])

    else: 
      self.name = [row for row in self.data.values if row[0] == self.factor_name and row[1] == self.sex and row[2] == self.age and row[4] == self.year and row[5] == self.month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])    

    
    return self.name
    '''

# 사용자가 입력한 변수만 통제하는 클래스 만들기 --> inpurt 값만 변수 통제에 사용할 수 있도록 하는 함수
class Classification():
  def __init__(self,data):
    self.data = data
   
    
  def split_factor(self,factor_name=False, sex=False, age=False, year=False, month=False):
    self.factor_name = factor_name
    self.sex = sex
    self.age = age
    self.year = year
    self.month = month

    start = {'소비업종':self.factor_name, "성별":self.sex, '연령대':self.age, "연도":self.year, '월별':self.month}
    key_list = []
    values_list = []
    
    for key, values in start.items():
      if values == False:
        continue
      else:
        key_list.append(key)
        values_list.append(values)

    a = self.data[key_list] == values_list
    b = self.data[a]

    return b

# 연도별 정리하기 
cov = covid_merss.소비일자.values
cov_mer = [str(row) for row in cov]
covid_merss['소비일자'] = cov_mer
covid_merss['연도'] = covid_merss['소비일자'].str[:4]
covid_merss['월별'] = covid_merss['소비일자'].str[5]
covid_merss = covid_merss.drop('소비일자', axis=1)
covid_merss

category = Classification(covid_merss)
data = category.split_factor(factor_name='요식/유흥',sex=False, age='30대',year='2019',month=False)
data

# 조합 경우의 수 구하기 및 클래스 확인
lists = ['소비업종','성별','연령대']
number = 2
a = []

for i in itertools.combinations(lists, number):
  b = list(i)
  a.append(b)
print(a)

c = [covid_merss[row] for row in a]
e = covid_merss[a[2]]
e

# 클래스 함수 확인용
factor_name = '요식/유흥'
sex = False
age = '30대'
year = '2019'
month = False
start = {'소비업종':factor_name, "성별":sex, '연령대':age, "연도":year, '월별':month}
values_list = []
key_list = []

for key, values in start.items():
  if values == False:
    continue
  else:
    key_list.append(key)
    values_list.append(values)

a = covid_merss[key_list] == values_list

b = covid_merss[a]
b