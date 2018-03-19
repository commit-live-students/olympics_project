import pandas as pd
from pandas import DataFrame,Series
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

def q02_rename_columns(path):

    df = q01_load_data(path)

    new_header = Series(df.columns)
    new_header[new_header.values == '01 !']  = 'Gold'
    new_header[new_header.values == '02 !'] = 'Silver'
    new_header[new_header.values == '03 !'] = 'Bronze'

    df.columns = new_header

    return df

q02_rename_columns("data/olympics.csv")
