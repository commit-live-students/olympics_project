# %load q04_country_with_most_gold_medals/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals


def q04_country_with_most_gold_medals(path):
    'write your solution here'
    df = q03_summer_gold_medals(path)
    df_gold = df['Gold']
    max_gold = df_gold.iloc[:,[-1]]
    max_gold = max_gold.astype(np.int)
    max_val = max_gold['Gold'].max()
    
    #return df_gold.iloc[:,[-1]]['Gold'] == 97
    name = max_gold.index[max_gold['Gold'] == max_val].tolist()
    name1 = name[0]
    return name1.split('\xa0')[0]   

q04_country_with_most_gold_medals('./data/olympics.csv')



