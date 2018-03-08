# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    'write your solution here'
    df = q02_rename_columns(path)
    cname = df.loc[:,'country name']
    for i in range(1,cname.shape[0]):
        cname[i] = cname[i].split('(')[0].rstrip()

    df1 = df.drop(labels='country name',axis=1)
    df1.index = cname
    df2 = df1.drop(labels='Totals',axis=0)
    return df2
   

