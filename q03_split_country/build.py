import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    "write your solution here"
    df = q02_rename_columns(path)

    #To split the country name into name and code based on '('
    new_columns = pd.DataFrame(df['country name'].str.split('(',1).tolist(), columns=['country_name','country_code'])

    #drop existing country name column
    df= df.drop(['country name'], axis=1)

    #Add new column country name based on above split step
    df.loc[:,'country name']=new_columns['country_name']

    #set the newly added country name column as index.
    df = df.set_index(keys=['country name'])

    return df[:-1]
