import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q05_difference_in_gold_medal(path):
    df = q02_rename_columns(path)
    dfnew = pd.DataFrame()
    dfnew['Summer_gold'] = df.iloc[:,2:3].astype(int)
    dfnew['Winter_gold'] = df.iloc[:,7:8].astype(int)
    dfnew['country'] = df['country name']
    dfnew['diff'] = abs(dfnew['Summer_gold'] - dfnew['Winter_gold'])
    country_diff = (dfnew.loc[dfnew['diff'].idxmax()])[3]
    #country_diff.replace("\xc2\xa0", " ")
    return country_diff
