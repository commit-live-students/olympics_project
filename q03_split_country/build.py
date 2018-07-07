import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    "write your solution here"
    df = q02_rename_columns(path)
    new_col = df['country name'].str.split('(').str.get(1).str.translate(None, ",!.; -@!%^&*)(").str.split('[').str.get(0)
    df.insert(loc=0, column='Code', value=new_col)
    df.index = df['country name'].str.split('(').str.get(0)
    #del df['country name']
    del df['Total']
    df.drop('Totals',axis=0,inplace = True)
    return df
