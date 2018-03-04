# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
from unittest import TestCase
from inspect import getargspec

def q06_get_points(path):
    'write your solution here'
    df = q02_rename_columns(path) 
    df = df[:-1]
    df['Points']=np.sum( df['Gold'].astype(int)  * 3  , axis=1) +   np.sum( df['Silver'].astype(int) * 2  , axis=1) +   np.sum( df['Bronze'].astype(int)    , axis=1)
    return df['Points']                                            
                                
                    
    
arg = getargspec(q06_get_points).args
                                
path = 'data/olympics.csv'
df = q06_get_points(path)
values = list(df[:10].values)
print values



