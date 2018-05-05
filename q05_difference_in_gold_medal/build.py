# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
import math

def q05_difference_in_gold_medal(path):
    'write your solution here'
    df= q02_rename_columns(path)
    df=df[:-1]
    df['bigg']= df['Gold'].iloc[:,0].astype(np.int16)-df['Gold'].iloc[:,1].astype(np.int16)
    tmp=df['bigg']
    #return df.loc[tmp.idxmax(),'country name'].strip()
    return tmp.max()

q05_difference_in_gold_medal('./data/olympics.csv')


