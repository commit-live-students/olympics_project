# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'
def q03_summer_gold_medals(path):
    'write your solution here'
    df = q02_rename_columns(path)
    country_name = df['country name'].str.split('(',expand=True)
    name = country_name[0]
    code = country_name[1]
    df['country name']=name
    df = df.set_index('country name')
    df = df.drop('Totals',axis=0)
    return df

q03_summer_gold_medals(path)
   

