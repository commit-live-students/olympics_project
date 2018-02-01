import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

def q02_rename_columns(path):
    "write your solution here"
    df = q01_load_data(path)
    frow = np.array(df.columns.values)
    frow = np.where(frow=='01 !','Gold',frow)
    frow = np.where(frow=='02 !','Silver',frow)
    frow = np.where(frow=='03 !','Bronze',frow)
    df.columns = frow
    return df
