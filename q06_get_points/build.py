# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'


def q06_get_points(path):
    df= q02_rename_columns(path)
    g=df['Gold'].iloc[:,2].astype(np.int16)*3
    b=df['Bronze'].iloc[:,2].astype(np.int16)*1
    s=df['Silver'].iloc[:,2].astype(np.int16)*2
    df['Points']=g+b+s
    return df['Points']



q06_get_points(path)



