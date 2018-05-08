# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q05_difference_in_gold_medal(path):
    df = q02_rename_columns(path)  
    df_countries = df.iloc[:-1,[0,2,7]]
    df_summer = pd.Series(df_countries.iloc[:,1]).astype(np.int)
    df_winter = pd.Series(df_countries.iloc[:,2]).astype(np.int)
    df_diff = abs(df_summer - df_winter)
    max_val = df_diff.max()
    res_arr = df_diff.values
    res_ind = np.where(res_arr == max_val)
    res_ind = res_ind[0][0]
    country_name = df_countries['country name'][res_ind + 1]
    return country_name.split('\xa0')[0]
q05_difference_in_gold_medal('./data/olympics.csv')


