# %load q02_rename_columns/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

def q02_rename_columns(path):
    'write your solution here'
    df = q01_load_data(path)
    df_rename=df
    df_rename=df_rename.rename(columns={'03 !':'Bronze','02 !':'Silver','01 !':'Gold'})
    #print(df.columns.values)
    return (df_rename)
#path='./data/olympics.csv'
#q02_rename_columns(path)

