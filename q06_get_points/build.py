import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
path = "data/olympics.csv"

def q06_get_points(path):
    "write your solution here"
    df = q02_rename_columns(path)
    df1 = df.loc[:,['country name','Gold','Silver','Bronze']]
    df2 = df1.iloc[:,[0,3,6,9]]
    df3 = df2
    df3 = df3.loc[:,['Gold','Silver','Bronze']].apply(pd.to_numeric)
    df3['Points'] = df3.loc[:,'Gold']*3 + df3.loc[:,'Silver']*2 + df3.loc[:,'Bronze']*1
    df3.drop(labels=['Gold','Silver','Bronze'],axis=1,inplace=True)
    df4 = df3.iloc[:,0] * 2
    df4.drop(labels=147,axis=0,inplace=True)
    return df4

#print q06_get_points(path)
