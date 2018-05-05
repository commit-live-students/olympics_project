# %load q02_rename_columns/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

path= './data/olympics.csv'
def q02_rename_columns(path):
    'write your solution here'
    df = q01_load_data(path)
    data_header = list(df.columns.values)
    for i in range(0,len(data_header),1):
        if(str(data_header[i])=='01 !'):
            data_header[i]='Gold'
        if(str(data_header[i])=='02 !'):
            data_header[i]='Silver'
        if(str(data_header[i])=='03 !'):
            data_header[i]='Bronze'
    df=df[1:]
    df.columns=data_header
    return df

