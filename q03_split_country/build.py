import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    "write your solution here"
    df = q02_rename_columns(path)
    df['country name']=df['country name'].apply(lambda x: x.split('(')[0])
    new_index=df['country name']
    df.drop(['country name'],axis=1,inplace=True)
    df.index=new_index
    df.drop(labels='Totals', axis=0,inplace=True)
    return df
