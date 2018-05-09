import numpy as np
import pandas as pd
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path='./data/olympics.csv'
def q05_difference_in_gold_medal(path):
    df=q02_rename_columns(path)
    country_names =[x.split('(')[0] for x in df.iloc[:,0]]
    df.set_index(pd.Series(country_names),inplace=True)
    df.drop(['country name'], axis = 1, inplace = True)
    df.drop(['Totals'], axis = 0, inplace = True)
    diff = (df.iloc[:,1].astype(int) - df.iloc[:,6].astype(int))
    return diff.max()


q05_difference_in_gold_medal(path)

