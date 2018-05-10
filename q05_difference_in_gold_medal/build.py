# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q05_difference_in_gold_medal(path):
    df = q02_rename_columns('./data/olympics.csv')
    df.rename(index=df['country name'],inplace=True)
    df = df[:-1]
    return (df.iloc[:,2].astype(np.int) - df.iloc[:,7].astype(np.int)).max()
q05_difference_in_gold_medal('./data/olympics.csv')


