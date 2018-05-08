# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'

def q06_get_points(path):
    df = q02_rename_columns(path)
    df['Points'] = ((df.iloc[:,12].astype(np.int)*3) + (df.iloc[:,13].astype(np.int)*2) + (df.iloc[:,14].astype(np.int)*1))
    df.drop('Combined total',axis=1,inplace=True)
    return df['Points']
    #return df

q06_get_points(path)






