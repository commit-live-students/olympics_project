import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q06_get_points(path):
    df = q02_rename_columns(path)
    wt = [3,2,1,3,2,1,3,2,1]
    df1 = df.iloc[:,[2,3,4,7,8,9,12,13,14]].astype(int)
    res = df1.mul(wt)
    df['Points'] = res.sum(axis=1)
    return res.sum(axis=1) 
