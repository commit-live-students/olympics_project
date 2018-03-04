# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
from unittest import TestCase
from inspect import getargspec

def q05_difference_in_gold_medal(path):
    'write your solution here'
    
    df = q02_rename_columns(path)
    df=df[:-1] #Drop last row which is total of all individual columns

    df['diff_max'] = pd.DataFrame(df.iloc[:,2].astype('int64')) - pd.DataFrame(df.iloc[:,7].astype('int64'))
    return df['diff_max'].max()
                         

arg = getargspec(q05_difference_in_gold_medal).args
print len(arg)
df = q05_difference_in_gold_medal('./data/olympics.csv')
print df
    



