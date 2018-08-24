# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    'write your solution here'
    df = q02_rename_columns(path)
    a = df['country name']
    b = a.str.split('(',expand=True)
    c = b[0]
    d = b[1]
    e = d.str.split(')', expand=True)
    f = list(e[0])
    df = df.set_index(c)
#     df['country code'] = f
    df.drop(['Totals'], axis = 0, inplace = True)
    df.drop(['country name'], axis = 1, inplace = True)
    df.index.name = 'country name'
    return df

# path = 'data/olympics.csv'
# q03_summer_gold_medals(path)


