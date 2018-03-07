import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q03_summer_gold_medals(path):
    df = q02_rename_columns(path="./data/olympics.csv")
    c = []
    "write your solution here"
    for i in df['country name']:
        n_co = i.split('(')[0].rstrip()
        c.append(n_co)
    df['country name'] = c
    ndf = df.set_index('country name')
    fdf = ndf.drop('Totals')
    return fdf
