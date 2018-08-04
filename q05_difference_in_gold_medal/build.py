# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
path = './data/olympics.csv'
def q05_difference_in_gold_medal(path):
    df = q02_rename_columns(path)
    d = df.Gold
    v = abs(d.iloc[:,0].astype(int) - d.iloc[:,1].astype(int))
    return v.nlargest(2).iloc[1,]
    




