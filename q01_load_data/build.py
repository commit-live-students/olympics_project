# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def q01_load_data(path):
    df = pd.read_csv(path,header = 0)
    df.loc[0][0] = 'country name'
    df.columns = df.loc[0]
    df = df.drop(0)
    return (df)

q01_load_data('./data/olympics.csv')


