# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

path = './data/olympics.csv'
def q01_load_data(path):
    df = pd.read_csv(path,header=0, skiprows=1)
    # use .read_csv function to read the
    # data and header=0 to skip the first row
    c = list(df.columns)
    c [0] = 'country name'
    df.columns = c
    return df

df = q01_load_data(path)
type(df)
df.shape


