import os
import pandas as pd
from glob import glob

with open('../dd.txt', 'r') as file:
    list1 = [] # 신문
    list2 = [] # 개수

    path = "C:/Users/USER/Desktop/CSV/"
    for i in os.listdir("C:/Users/USER/Desktop/CSV/"):

        df = pd.read_csv(path+i)

        f = i.split(".")
        list1.append(f[0])
        list2.append(str(len(df)))

    file_content = file.read()
    file_content = file_content.split("\n")
    print(file_content)
    for i in file_content:

        if i not in list1:
            list1.append(i)
            list2.append("0")

    date = {
        "검색어" : list1,
        "검색 개수" : list2

    }
    total = pd.DataFrame(date)
    total.to_csv("C:/Users/USER/Desktop/CSV/res.csv", index=False, encoding='utf-8-sig')