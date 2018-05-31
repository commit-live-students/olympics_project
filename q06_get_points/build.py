# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'

def q06_get_points(path):
    df = q02_rename_columns(path)
    df1 = df.iloc[:,[2,7,12]].astype(int).sum(axis=1)*[3]
    df2 = df.iloc[:,[3,8,13]].astype(int).sum(axis=1)*[2]
    df3 = df.iloc[:,[4,9,14]].astype(int).sum(axis=1)
    df['Points']= ((df1+df2+df3)/2).astype(int)
    return df['Points']



