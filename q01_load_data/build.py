# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def q01_load_data(path):
    'write your solution here'
    # use .read_csv function to read the
    # data and header=0 to skip the first row
    df = pd.read_csv(path, header=0)
    new_header = df.iloc[0]  # grab the first row for the header
    new_header[0] = 'country name'
    df = df[1:]  # take the data less the header row
    df.columns = new_header  # set the header row as the df header
    return df


path = 'data/olympics.csv'
q01_load_data(path)


