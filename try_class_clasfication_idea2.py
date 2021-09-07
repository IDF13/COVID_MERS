# 사용자가 입력한 변수는 조건부로,
# 입력하지 않은 변수는 모두 포함한 데이터 프레임 분류기 클래스이다.
# 단, 경우의 수가 많아지면 힘들다...

class Classification_all():
  def __init__(self,name, data):
    self.name = name
    self.data = data
   
    
 
  def split_factor(self,factor_name, sex=False, age=False, year=False, month=False):

    self.name = [row for row in self.data.values if row[0] == factor_name and row[1] == sex and row[2] == age and row[4] == year and row[5] == month]
    self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])  
 
    if sex == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[2] == age and row[4] == year and row[5] == month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])

    if age == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[1] == sex and row[4] == year and row[5] == month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])

    if year == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[1] == sex and row[2] == age and row[5] == month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])

    if month == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[1] == sex and row[2] == age and row[4] == year]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])

    if sex == False and age == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[4] == year and row[5] == month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])  

    if sex == False and year == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[2] == age and row[5] == month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])    

    if sex == False and month == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[2] == age and row[4] == year]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])   

    if age == False and year == False: 
      self.name = [row for row in self.data.values if row[0] == factor_name and row[1] == sex and row[5] == month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])      

    if age == False and month == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[1] == sex and row[4] == year]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])         
    
    if year == False and month == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[1] == sex and row[2] == age]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])      

    if sex == False and age ==False and year==False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[5] == month]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])    
    
    if sex == False and age == False and month == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[4] == year]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])    
    
    if sex == False and year == False and month == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[2] == age]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])         
    
    if age == False and year ==False and month == False:
      self.name = [row for row in self.data.values if row[0] == factor_name and row[1] == sex]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])         

    if sex == False and age == False and year == False and month == False:
      self.name = [row for row in self.data.values if row[0] == factor_name]
      self.name = pd.DataFrame(self.name, columns=['업종','성별','나이','소비 합계','연도','월'])
        
    return self.name



# 조합 경우의 수 구하여 클래스 정의 하는데 실수가 없게 하기 위해서 사용
import itertools
lists = ['전부','전연령','3년','3개월']
number = 3
a = []

for i in itertools.combinations(lists, number):
  b = list(i)
  a.append(b)
print(a)


