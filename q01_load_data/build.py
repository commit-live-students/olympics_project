import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def q01_load_data(path):
    dd=pd.read_csv(path,header=0)
    header=dd.iloc[0]
    header[0]='Country Name'
    new_df=dd[1:]
    new_df.columns=header
    return new_df
