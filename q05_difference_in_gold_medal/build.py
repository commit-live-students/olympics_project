# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q05_difference_in_gold_medal(path):
    'write your solution here'
    df = q02_rename_columns(path)
    df = df.drop([147])
    dfGold = df['Gold']
    print(dfGold.iloc[:,0].astype('int').max())
    print(dfGold.iloc[:,0].astype('int').min())
    diff = dfGold.iloc[:,0].astype('int') - dfGold.iloc[:,1].astype('int')
    diffIndex = diff.idxmax()
    print(diff.max())
    return diff.max()
q05_difference_in_gold_medal('./data/olympics.csv')

