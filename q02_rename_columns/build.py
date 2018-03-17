import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

path = "data/olympics.csv"
def q02_rename_columns(path):
    "write your solution here"
    df = q01_load_data(path)
    #new_header = df.iloc[1]
    df1 = df.rename(columns={'01 !': 'Gold', '02 !': 'Silver', '03 !':'Bronze'})

    return (df1)
#q02_rename_columns(path)
