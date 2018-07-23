# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
path = './data/olympics.csv'
def q05_difference_in_gold_medal(path):
    df = q02_rename_columns(path)
    df_gold_medals = df.iloc[:,[0,2,7]]
    df_gold_medals_new = df_gold_medals.iloc[:,[1,2]].astype(int)
    df_gold_medals.drop(labels=['Gold'],axis=1, inplace=True)
    df_gold_medals_new = pd.concat([df_gold_medals_new, df_gold_medals], axis=1)
    df_gold_medals_new['Difference'] = df_gold_medals_new.iloc[:,0] - df_gold_medals_new.iloc[:,1]
    df_gold_final = df_gold_medals_new.iloc[:,[2,3]][0:146]
    return df_gold_final[df_gold_final['Difference'] == df_gold_final['Difference'].max()].iloc[0,1]

q05_difference_in_gold_medal(path)


