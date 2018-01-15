import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# import sys
# import os
#
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'


def q03_summer_gold_medals(path):
    "write your solution here"
    df = q02_rename_columns(path)
    df['country name'] = df.ix[:, 0].str.rpartition('(')[0].str.replace("(", " ")

    # setting country name as index
    df = df.set_index('country name')

    # removing the extra characters
    df.ix[:, 0] = df.ix[:, 0].apply(lambda x: x.split('(', 1)[0])

    # dropping the columns totals
    return df[:-1]


print(q03_summer_gold_medals(path).shape)