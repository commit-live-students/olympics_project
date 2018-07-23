# %load q06_get_points/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = './data/olympics.csv'
def q06_get_points(path):
    df = q02_rename_columns(path) 
    df_gsb = df.iloc[:,[2,3,4,7,8,9,12,13,14]]
    df_gsb = df_gsb.astype('int')
    df_gsb['Total_Gold'] = df_gsb.iloc[:,0] + df_gsb.iloc[:,3] + df_gsb.iloc[:,6]
    df_gsb['Total_Silver'] = df_gsb.iloc[:,1] + df_gsb.iloc[:,4] + df_gsb.iloc[:,7]
    df_gsb['Total_Bronze'] = df_gsb.iloc[:,2] + df_gsb.iloc[:,5] + df_gsb.iloc[:,8]
    df_gsb['Points'] = df_gsb['Total_Gold']*3 + df_gsb['Total_Silver']*2 + df_gsb['Total_Bronze']*1
    
    return (df_gsb['Points'])
q06_get_points(path)

