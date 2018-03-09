# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
path='./data/olympics.csv'


def q05_difference_in_gold_medal(path):
    l1 = []
    l2 = []
    df = q02_rename_columns(path)
    summer = df.iloc[:,2]
    winter = df.iloc[:,7]
    for i in summer:
        l1.append(int(i))
    for j in winter:
        l2.append(int(j))

    big_dif =  [abs(x - y) for x, y in zip(l1, l2)] 
    df['Summer - Winter']= big_dif

    df.drop(axis = 0,labels = [147],inplace = True)
    diff = df['Summer - Winter'].max()
    return diff

q05_difference_in_gold_medal(path)


# def q05_difference_in_gold_medal(path):
#     df = q02_rename_columns(path)
#     'write your solution here'
#     return max(abs(df.iloc[:-1,2].astype(int) - df.iloc[:-1,7].astype(int)))
# #q05_difference_in_gold_medal(path)



