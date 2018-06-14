# %load q03_split_country/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
import re

path = './data/olympics.csv'
df_new = []

def q03_summer_gold_medals(path):
    'write your solution here'
    df = q02_rename_columns(path)
    #df = pd.DataFrame(df, index = 'country')
    
    country = []
    code = []
    
    for name in df['country name']:
        country.append((name.split()[0]))
        code.append(''.join(re.findall('\(\w{3}\)', name)))
        
    df.index = country
    df.drop(labels = ['Combined total'], axis = 1, inplace = True)
    df.drop(labels = ['Totals'], axis = 0, inplace = True)
    #for name in df['country name']:
    #    country.append((name.split()[0], ''.join(re.findall('\(\w{3}\)', name))))
    #for i in range(1,lene.(df)+1):
    return df
        
        #df_new.append(df.loc[i,'country name'].split())
        #country = df.loc[i, 'country name'].split()
   #print(df.loc[i, 'country name'].str.contains('\(\w{3}\)'))
        
    
    
   








