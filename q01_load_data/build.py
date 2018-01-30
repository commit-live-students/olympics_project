import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def q01_load_data(path):
    data = pd.read_csv(path,skiprows = [0])
    header = list(data)
    header[0] = 'Country Name'
    data.columns = header
    return data
