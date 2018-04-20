# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'
def q05_difference_in_gold_medal(path):
    'write your solution here'
    df = q02_rename_columns(path)
    df = df[:-1]
    df1 = df.rename(columns={'01 !': 'Gold', '02 !': 'Silver', '03 !':'Bronze'})
    df_Sumer = pd.to_numeric(df1.iloc[:, 2])
    df_win = pd.to_numeric(df1.iloc[:, 7])
    df_1 = (df_Sumer) - (df_win)
    return (df_1).max() 
q05_difference_in_gold_medal(path)



