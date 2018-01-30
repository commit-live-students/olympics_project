import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns


def q03_summer_gold_medals(path):
    df = q02_rename_columns(path)
    df['country name'] = df['country name'].str.split('(',expand = True)
    df.set_index('country name',inplace = True)
    df.drop('Totals',inplace = True)
    return df
