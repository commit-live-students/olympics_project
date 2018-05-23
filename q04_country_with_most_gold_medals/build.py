import pandas as pd
import numpy as np
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = './data/olympics.csv'
def q04_country_with_most_gold_medals(path):
    df = q02_rename_columns(path)
    country_names =[x.split('(')[0] for x in df.iloc[:,0]]
    df.set_index(pd.Series(country_names),inplace=True)
    #df.drop(['country name'], axis = 1, inplace = True)
    df.drop(['Totals'], axis = 0, inplace = True)
    max_gold_list  = df.groupby(['country name'])['Gold'].sum()
    df2 = max_gold_list.groupby(['country name']).sum()
    return df2.idxmax()

q04_country_with_most_gold_medals(path)

