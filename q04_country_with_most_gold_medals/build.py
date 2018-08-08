# %load q04_country_with_most_gold_medals/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals

path = 'data/olympics.csv'
def q04_country_with_most_gold_medals(path):
    'write your solution here'
    df = q03_summer_gold_medals(path)
    df1 = df.loc[:,'Gold']
    df1.iloc[:,:] = df1.iloc[:,:].apply(pd.to_numeric)
    df2 = df1.iloc[:,:].sum(axis=1)
    return df2[df2 == df2.max()].index[0]
    

#print(q04_country_with_most_gold_medals(path))



