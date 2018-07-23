# %load q04_country_with_most_gold_medals/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals
path = './data/olympics.csv'

def q04_country_with_most_gold_medals(path):
    df = q03_summer_gold_medals(path)
    df_gold_count = df.iloc[:,[1,6,11]]
    df_gold_count = df_gold_count.astype('int')
    df_gold_count['Total'] = df_gold_count.sum(axis=1)
    df_gold_final =  df_gold_count.iloc[:,-1].reset_index()
    df_gold_final = df_gold_final[df_gold_final['Total'] == df_gold_final.Total.max()]
    return df_gold_final.iloc[0,0]
q04_country_with_most_gold_medals(path)
    




