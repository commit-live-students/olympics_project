# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'
def q06_get_points(path):
    df = q02_rename_columns(path)
    df['Points'] = df['Gold'].iloc[:,-1].astype('int') * 3 + df['Silver'].iloc[:,-1].astype('int') * 2 + df['Bronze'].iloc[:,-1].astype('int') * 1
    return df['Points']

q06_get_points(path)



