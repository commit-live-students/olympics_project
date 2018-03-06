# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'


def q03_summer_gold_medals(path):
    "write your solution here"
    df = q02_rename_columns(path)
    df1 = pd.DataFrame(df['country name'].str.split('(').tolist(),columns=['country name','country code'])
    df1.index = np.arange(1,len(df1)+1)
    df = df.drop(['country name'],axis=1)
    df = pd.concat([pd.DataFrame(df1['country name']),df],axis=1)
    df = df.set_index('country name')
    df = df.drop(['Totals'])
    return df

q03_summer_gold_medals(path)
