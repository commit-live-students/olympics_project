import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
path = "data/olympics.csv"

def q01_load_data(path):
    "write your solution here"
    df = pd.read_csv(path)
    frow = df.iloc[0,:]
    frow[0] = "country name"
    df = df.iloc[1:,:]
    df.columns = frow
    return df
