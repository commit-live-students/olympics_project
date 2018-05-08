# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

path = './data/olympics.csv'

def q01_load_data(path):
    'write your solution here'
    my_df = pd.read_csv(path,header=0)
    my_header = my_df.iloc[0]
    my_header[0] = 'country name'
    my_df = my_df[1:]
    my_df.columns = my_header
    return my_df
q01_load_data(path)




