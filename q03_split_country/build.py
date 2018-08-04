# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = './data/olympics.csv'
def q03_summer_gold_medals(path):
#     'write your solution here'
    df = q02_rename_columns(path)
    country_names = df['country name']
    s = country_names.apply(lambda x : x.split()[0])
    df['country'] = s
    df.set_index('country', inplace=True)
#     df.drop(['Total'], axis=1, inplace=True)
    df.drop(['country name'], axis=1, inplace=True)
    return df[:-1]
df = q03_summer_gold_medals(path)
df.shape


