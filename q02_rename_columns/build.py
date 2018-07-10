# %load q02_rename_columns/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
#from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

def q02_rename_columns(path):
    'write your solution here'
    df = q01_load_data(path)
    df.rename(columns={'01 !':'Gold','02 !':'Silver','03 !':'Bronze'},inplace=True)
    return df

def q01_load_data(path):
    "write your solution here"
    df = pd.read_csv(path, header=0)
    new_header = df.iloc[0]  # grab the first row for the header
    new_header[0] = 'country name'
    df = df[1:]  # take the data less the header row
    df.columns = new_header  # set the header row as the df header
    return df

df = q02_rename_columns('data/olympics.csv')
