#%load q01_load_data/build.py
import pandas as pd
import numpy as np

path ='./data/olympics.csv'
def q01_load_data(path):
    data = pd.read_csv(path)
    data_header = data.iloc[0]
    data=data[1:]
    data_header[0]='country name'
    data.columns=data_header
    return data


