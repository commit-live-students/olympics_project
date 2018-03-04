import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q06_get_points(path):
    "write your solution here"
    df = q02_rename_columns(path)
    df['Gold']= df['Gold'].astype(int)
    df['Silver']= df['Silver'].astype(int)
    df['Bronze']= df['Bronze'].astype(int)

    df['points']=np.sum( df['Gold']  * 3  , axis=1) +   np.sum( df['Silver'] * 2  , axis=1) +   np.sum( df['Bronze'] *1    , axis=1)
    return df['points']
