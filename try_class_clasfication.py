import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = '/content/drive/MyDrive/ML Deep/'
COVID_MERSS = pd.read_csv(path + "DATA_SSC_CORONA_MERS.csv")
 
covid_merss = pd.DataFrame(COVID_MERSS)
covid_merss


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
    c = b.dropna(axis = 1, how='all')
    d = c.dropna(axis = 0, how='any')

    return d

# 연도별 정리하기 
cov = covid_merss.소비일자.values
cov_mer = [str(row) for row in cov]
covid_merss['소비일자'] = cov_mer
covid_merss['연도'] = covid_merss['소비일자'].str[:4]
covid_merss['월별'] = covid_merss['소비일자'].str[5]
covid_merss = covid_merss.drop('소비일자', axis=1)
covid_merss

# 클래스 적용
category = Classification(covid_merss)
data = category.split_factor(factor_name='요식/유흥',sex=False, age='30대',year='2019',month=False)
data

