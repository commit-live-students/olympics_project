# %load q04_country_with_most_gold_medals/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals


def q04_country_with_most_gold_medals(path):
    'write your solution here'
    df = q03_summer_gold_medals(path)
    df1 = df.iloc[1:,[1,6,11]].astype(int).sum(axis = 1).sort_values(ascending = False).reset_index()
    return df1['country name'][0].replace('\xa0','')



