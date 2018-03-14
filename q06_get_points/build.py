
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# import sys
# import os
#
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'
def q06_get_points(path):
    'write your solution here'
    df = q02_rename_columns(path) #get the data
    df['Gold Total'] = df[['Gold']].astype(int).sum(1).apply(lambda x: x * 3) # create a column for Gold total
    df['Silver Total'] = df[['Silver']].astype(int).sum(1).apply(lambda x: x * 2)
    df['Bronze Total'] = df[['Bronze']].astype(int).sum(1).apply(lambda x: x * 1)
    df['Points'] = df['Gold Total'].astype(int) + df['Silver Total'].astype(int) + df['Bronze Total'].astype(int)
    df = df.drop(['Gold Total', 'Silver Total', 'Bronze Total'], axis=1)
    return df['Points']

