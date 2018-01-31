import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
path = "data/olympics.csv"

def q05_difference_in_gold_medal(path):
    "write your solution here"
    df = q02_rename_columns(path)
    df1 = df.loc[:,['country name','Gold']]
    df2 = df1.iloc[:,[0,1,2]]
    df3 = df2.set_index(keys='country name')
    df3.loc[:,:] = df3.loc[:,:].apply(pd.to_numeric)
    df3.drop(['Totals'],inplace=True)
    df4 = df3.iloc[:,0] - df3.iloc[:,1]
    df4 = df4.abs()
    print df4
    return df4[df4==df4.max()].index[0].split("[")[0].rstrip()

print q05_difference_in_gold_medal(path)
