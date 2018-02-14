import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q06_get_points(path):
    df = q02_rename_columns(path)
    df.iloc[:,12:15] = df.iloc[:,12:15].apply(pd.to_numeric)
    df['Points1'] = (df.iloc[:,12:13] * 3)
    df['Points2'] = (df.iloc[:,13:14] * 2)
    df['Points3'] = (df.iloc[:,14:15] * 1)
    df['Points'] = df['Points1']+df['Points2']+df['Points3']
    df['Points'] = df['Points']*2
    return (pd.Series(df['Points'])) 
