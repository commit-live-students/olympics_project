import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    "write your solution here"
    df = q02_rename_columns(path)
    country_cols=pd.DataFrame (
                        df['country name'].str.split('(',1).tolist()
                        , columns=['country name','country code'])
    df= df.drop(['country name'], axis=1)
    df.loc[:,'country name']=country_cols['country name']
    df = df.set_index(keys=['country name'])
    return df[:-1]
