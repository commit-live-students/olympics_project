# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    'write your solution here'
    df = q02_rename_columns(path)
    df_country = df['country name'].str.split('(',expand=True)
    #df_country.drop('country name', axis=1, inplace=True)
    #df_country = df_country[0]
    #df['country name'] = df_country
    #df.set_index('country name',inplace=True)
    #df.drop('Totals', axis = 1, inplace=True)
    return df_country[0]
q03_summer_gold_medals('./data/olympics.csv')   


