# %load q02_rename_columns/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

def q02_rename_columns(path):
    'write your solution here'
    df = q01_load_data(path)
    #print(df.columns)
    colList = list(df.columns)
    #df['01 !']
    #print(colList)
    for n, i in enumerate(colList):
        #print(n)
        #print(i)
        if '01' in i:
            colList[n] = 'Gold'
        elif '02' in i:
            colList[n] = 'Silver'
        elif '03' in i:
            colList[n] = 'Bronze'
    #print(colList)
    df.columns = colList
    return df.head(5)
q02_rename_columns('./data/olympics.csv') 

