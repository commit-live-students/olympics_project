import pandas as pd
from pandas import Series
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):

    df = q02_rename_columns(path)

    data = df.iloc[:,0]
    data1 = data.str.split('(')

    index = Series()

    for i in range(0,data1.shape[0]):
        # append first element of each list to the index
        index = index.append(pd.Series(data1.iloc[i][0]))

    df.index = index

    df = df.drop(['Totals'], axis = 0)
    df = df.drop(['country name'], axis = 1)

    return df
