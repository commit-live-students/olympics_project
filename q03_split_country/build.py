# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    'write your solution here'
    df = q02_rename_columns(path)
    #print(df.head())
    df_redit=df
    for a in df_redit:
        print(df_redit[a])
    #print(df['country name'])
path='./data/olympics.csv'
#q03_summer_gold_medals(path)

