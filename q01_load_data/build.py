import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pep8


def q01_load_data(path):
    df = pd.read_csv(path, header=0, skiprows=1)
    df = df.rename(columns={'Unnamed: 0': 'country name', })
    return df
