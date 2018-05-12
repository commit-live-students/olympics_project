# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'

def q06_get_points(path):
    df = q02_rename_columns(path)
    #df = df[:-1]   #removed last row Totals
    #calculate points
    #points_gold = df['Gold'].astype(np.int).sum(axis=1)
    points_gold = (df.iloc[:,2:3].astype(np.int).sum(axis=1)+(df.iloc[:,7:8].astype(np.int).sum(axis=1)))*3
    #points_silver = df['Silver'].astype(np.int).sum(axis=1)
    points_silver = (df.iloc[:,3:4].astype(np.int).sum(axis=1)+(df.iloc[:,8:9].astype(np.int).sum(axis=1)))*2
    #points_bronze = df['Bronze'].astype(np.int).sum(axis=1)
    points_bronze = (df.iloc[:,4:5].astype(np.int).sum(axis=1)+(df.iloc[:,9:10].astype(np.int).sum(axis=1)))
    #print(points_gold)
    #print(points_silver)
    #print(points_bronze)
    df['Points'] = (points_gold.values) + (points_silver.values) + (points_bronze.values)
    
    return df['Points']

#q06_get_points(path)

