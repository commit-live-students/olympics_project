# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'

def q06_get_points(path):
    df = q02_rename_columns(path)
    g = df.Gold.astype(int) * 3
    s = df.Silver.astype(int) * 2
    b = df.Bronze.astype(int) * 1
    total_points = g.iloc[:,0] + g.iloc[:,1] + s.iloc[:,0] + s.iloc[:,1] +b.iloc[:,0] + b.iloc[:,1]
    df['Points'] = total_points
    return df.Points




