import pandas as pd
import numpy as np
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = './data/olympics.csv'
def q06_get_points(path):
    df = q02_rename_columns(path)
    wt = [3,2,1]
    df1 = df.iloc[:,[12,13,14]].astype(int)
    res = df1.mul(wt)
    df['Points'] = res.sum(axis=1)
    return res.sum(axis=1) 

q06_get_points(path)



