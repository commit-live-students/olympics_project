import pandas as pd
import numpy as np
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = './data/olympics.csv'
def q03_summer_gold_medals(path):
    df = q02_rename_columns(path)
    country_names =[x.split('(')[0] for x in df.iloc[:,0]]
    df.set_index(pd.Series(country_names),inplace=True)
    df.drop(['country name'], axis = 1, inplace = True)
    df.drop(['Totals'], axis = 0, inplace = True)
    return df

q03_summer_gold_medals(path)

