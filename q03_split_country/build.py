# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def split_func(value):
    value.strip(' ')
    value=value.split('(')
    return value[0].strip(' ')

   

def q03_summer_gold_medals(path):
    ##'write your solution here'
    df = q02_rename_columns(path)
    CC = df['country name'].apply(split_func)
    df['country name']=CC
    df.set_index('country name',inplace=True)
    df.drop(labels=['Totals'], axis=0,inplace=True)
    return df

