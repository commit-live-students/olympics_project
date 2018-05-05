# %load q02_rename_columns/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data
path = './data/olympics'
def q02_rename_columns(path):
    'write your solution here'
    df = q01_load_data(path)
    df = df.rename(index=str, columns={'01 !':'Gold','02 !':'Silver','03 !':'Bronze'})
    return df
q02_rename_columns(path = './data/olympics.csv')    


