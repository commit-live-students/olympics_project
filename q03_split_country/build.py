import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

#path = "data/olympics.csv"

def q03_summer_gold_medals(path):
    df = q02_rename_columns(path)
    df['country name'],df['country code']=df['country name'].str.split('(',1).str
    df.set_index('country name',inplace=True)
    del df['Combined total']
    return df[1:147]
