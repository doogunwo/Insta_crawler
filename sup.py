import pandas as pd
# 7507개/ 12000개
import pandas as pd
from glob import glob

file_names = glob("C:/Users/USER/Desktop/CSV/*.csv") #폴더 내의 모든 csv파일 목록을 불러온다
print(file_names)
total = pd.DataFrame() #빈 데이터프레임 하나를 생성한다

for file_name in file_names:
    temp = pd.read_csv(file_name, encoding='utf-8')
    total = pd.concat([total, temp]) #전체 데이터프레임에 추가하여 넣는다
print(total)
total.to_csv("C:/Users/USER/Desktop/CSV/total.csv",index=False,encoding='utf-8-sig')
