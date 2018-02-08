import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    df = q02_rename_columns(path)
    country = []
    for i in df['country name']:
        i = i.rsplit('(')[0]
        i = i.replace("\xc2\xa0", "")
        country.append(i)
    df['country name']= country

    df = df.set_index('country name')
    df = df.drop(['Totals'])
    return df
