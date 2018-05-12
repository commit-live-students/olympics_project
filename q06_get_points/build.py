# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'

def q06_get_points(path):
    df = q02_rename_columns(path)
    return df.iloc[:,-4].astype(np.int) * 3 + df.iloc[:,-3].astype(np.int) * 2 + df.iloc[:,-2].astype(np.int)


