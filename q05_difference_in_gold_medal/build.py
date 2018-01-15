import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# import sys
# import os
#
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = 'data/olympics.csv'
def q05_difference_in_gold_medal(path):
    "write your solution here"
    df = q02_rename_columns(path)
    maxDiff = (df.ix[:, 2].astype(int) - df.ix[:, 6].astype(int)).abs().idxmax()

    return maxDiff

print(q05_difference_in_gold_medal(path))

