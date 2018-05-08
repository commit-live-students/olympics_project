# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q05_difference_in_gold_medal(path):
    'write your solution here'
    df = q02_rename_columns(path)
    df = df[:-1]
    a = df['Gold'].iloc[:,[0]].astype(np.int).sub(df['Gold'].iloc[:,[1]].astype(np.int))
    country = df['country name'].loc[a['Gold'].argmax()].replace('\xa0',' ')    
    return a['Gold'].max()
    
q05_difference_in_gold_medal('data/olympics.csv')



880 != 880 

