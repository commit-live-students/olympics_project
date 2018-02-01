import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q05_difference_in_gold_medal(path):
    df = q02_rename_columns(path)
    diff = df.iloc[:-1,2].astype(int) - df.iloc[:-1,7].astype(int)
    return diff.max()
