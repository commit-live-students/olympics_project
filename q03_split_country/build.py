# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    'write your solution here'
    df = q02_rename_columns(path)
    print(df.shape)
    print(df.columns)
    dfNew = pd.DataFrame(df['country name'].str.split('(',1).tolist(),
                                   columns = ['country name New','country code'])
    dfNew['country code'] = dfNew['country code'].astype('str')
    print(dfNew['country code'].dtype)
    countryCodeDF = pd.DataFrame(dfNew['country code'].str.split(')',1).tolist(),
                                   columns = ['country code Final','trash']) 
    mergedDF = df.join(dfNew)
    mergedDF = mergedDF.join(countryCodeDF)
    finalDF = mergedDF.drop(['country code','trash','country name','Combined total'],axis=1)
    finalDF = finalDF.rename(columns={'country name New': 'country name', 'country code Final': 'country code'})
    finalDF = finalDF.set_index('country name')
    print(finalDF.shape)
    print(finalDF.columns)
    finalDF = finalDF.dropna()
    return finalDF


q03_summer_gold_medals('./data/olympics.csv')     

