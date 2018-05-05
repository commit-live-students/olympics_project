import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
import re

def q03_summer_gold_medals(path):
    'write your solution here'
    df = q02_rename_columns(path)
    #tmp= df['country name'].apply(lambda x: re.findall('\((.*?)\)',x))
    df['country name']=df['country name'].str.replace(r'\(([A-Za-z0-9 _]+)\)', '')
    df['country name']=df['country name'].str.replace(r'\[([A-Za-z0-9_]+)\]', '')
    df.index=df['country name']
    df.drop(['country name','Totals'], axis=1,inplace=True)
    
    return df[:-1]

path='./data/olympics.csv'
q03_summer_gold_medals(path)

