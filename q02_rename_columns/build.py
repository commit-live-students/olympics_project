
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

#path = 'data/olympics.csv'
def q02_rename_columns(path):
    'write your solution here'
    df = q01_load_data(path)
    df.rename(columns=lambda x: 'Gold' if '01' in x else x, inplace=True)
    df.rename(columns=lambda x: 'Silver' if '02' in x else x, inplace=True)
    df.rename(columns=lambda x: 'Bronze' if '03' in x else x, inplace=True)
    return df

