# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def q01_load_data(path):
    'write your solution here'
    # use .read_csv function to read the
    # data and header=0 to skip the first row
    df = pd.read_csv(path, header=0)
    header = df.iloc[0]
    header[0] = 'country name'
    df = df.iloc[1:,:]
    df.columns = header
    return df
    



