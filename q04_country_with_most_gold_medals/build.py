# %load q04_country_with_most_gold_medals/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals
path='./data/olympics.csv'

def q04_country_with_most_gold_medals(path):
    'write your solution here'
    data = q03_summer_gold_medals(path)
    x,y=data.shape
    list1=[]
    for j in range(0,x,1):
        sum1=0
        for i in range(0,len(data.columns),1):
            if str(data.columns[i])=='Gold':
                sum1+=int(data.iloc[j,i])
    
        list1.append(sum1)
        
    max_val=max(list1)
    max_index=list1.index(max_val)
    data= data.reset_index()
    
    max_country=data.iloc[max_index,0]
        
    
    
    return max_country



