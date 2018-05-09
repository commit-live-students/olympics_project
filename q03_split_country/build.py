# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path='./data/olympics.csv'
def q03_summer_gold_medals(path):
    'write your solution here'
    df2 = q02_rename_columns(path)
    df2. rename(columns={'country name': 'country_name'}, inplace=True)
    df2['country name'] = df2['country_name'].str.split('(', 1).str.get(0)
    df2.set_index('country name', inplace=True)
    df2 = df2.drop('country_name', 1)
    df2 = df2.drop('Totals', 0)
    return df2

    

