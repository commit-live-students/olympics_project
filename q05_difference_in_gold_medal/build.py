# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'

def q05_difference_in_gold_medal(path):
    df = q02_rename_columns(path)
    #print pd.DataFrame(df.iloc[:,2]) - pd.DataFrame(df.iloc[:,7])
    cols = list(df.columns)
    cols[2] = 'SGold'
    cols[7] = 'WGold'
    cols[12]  = 'TGold'
    df.columns = cols
    df['diff'] = pd.to_numeric(df['SGold']) - pd.to_numeric(df['WGold'])
    df = df.drop(147)
    return max(df['diff'])
    #return df.iloc[135][0]


q05_difference_in_gold_medal(path)
