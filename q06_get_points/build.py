# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'
def q06_get_points(path):
    df = q02_rename_columns(path)
    gold_points = df['Gold'].iloc[:,2].astype(np.int) * 3
    silver_points = df['Silver'].iloc[:,2].astype(np.int) * 2
    bronze_points = df['Bronze'].iloc[:,2].astype(np.int)
    total_points = gold_points + silver_points + bronze_points
    df['Points'] = total_points
    df.drop('Combined total',axis=1,inplace=True)
    return total_points
q06_get_points(path)


