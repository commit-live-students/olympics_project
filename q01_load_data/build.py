# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def q01_load_data(path):
    'write your solution here'
    file = pd.read_csv(path,header=0)
    new_header = file.iloc[0]
    new_header[0]='country name'
    file = file[1:]
    file.columns = new_header
    return file
q01_load_data('./data/olympics.csv')

