import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'
def q06_get_points(path):
    df = q02_rename_columns(path)
    df = df.iloc[:, :-1]
    df_silver = (df['Silver']).astype(int)
    df_gold = (df['Gold']).astype(int)
    df_bronze = (df['Bronze']).astype(int)
    df['To'] = ((np.sum(df_gold * 3, axis=1) / 2) + (np.sum(df_silver * 2, axis=1)/2) + (np.sum(df_bronze * 1, axis = 1)) /2)       
    return (df['To'].astype(int))

q06_get_points(path)


