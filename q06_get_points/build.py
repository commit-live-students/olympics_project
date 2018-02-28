# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'


def q06_get_points(path):
    df = q02_rename_columns(path)
    cols = list(df.columns)
    cols[2] = 'SGold'
    cols[3] = 'SSilver'
    cols[4] = 'SBronze'
    cols[7] = 'WGold'
    cols[8] = 'WSilver'
    cols[9] = 'WBronze'
    cols[12]  = 'TGold'
    cols[13]  = 'TSilver'
    cols[14]  = 'TBronze'
    df.columns = cols
    df1 = pd.DataFrame()
    df['Points'] = ((pd.to_numeric(df['TGold']) * 3) + (pd.to_numeric(df['TSilver']) * 2) + (pd.to_numeric(df['TBronze']))) * 2
    return df['Points']

#q06_get_points(path)
