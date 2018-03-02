import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q05_difference_in_gold_medal(path):
    "write your solution here"
    df = q02_rename_columns(path)
    diff = df['Gold'].iloc[:-1,0].astype('int64') - df['Gold'].iloc[:-1,1].astype('int64')
    return diff.max()
