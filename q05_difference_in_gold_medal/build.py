# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q05_difference_in_gold_medal(path):
    'write your solution here'
    df=q02_rename_columns(path)
    cc=df['country name'].apply(lambda x : x.split('(')[0].strip(' '))
    df['country name']=cc
    df.set_index('country name',inplace=True)
    df.drop(labels='Totals',axis=0,inplace=True)
    diff=(df.iloc[:,1].astype(np.int64)-df.iloc[:,6].astype(np.int64)).abs()
    df['diff']=diff
    df.sort_values('diff',ascending=False,inplace=True)
    df.reset_index(inplace=True)
    return df.iloc[0,16]

