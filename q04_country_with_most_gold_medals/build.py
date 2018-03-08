# %load q04_country_with_most_gold_medals/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals

#path='./data/olympics.csv'
def q04_country_with_most_gold_medals(path):
    'write your solution here'
    df = q03_summer_gold_medals(path)
    gold_count = df.iloc[:,1].sort_values(ascending=False)

    df['gold_count'] = gold_count
    max = gold_count.max()
    a = df[df['gold_count'] == max]
    aa = a.index
    aaa = aa[0]
    return aaa
#q04_country_with_most_gold_medals(path)
    



