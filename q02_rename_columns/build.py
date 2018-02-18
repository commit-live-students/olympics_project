import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

def q02_rename_columns(path):
    "write your solution here"
    df = q01_load_data(path)
    return df.rename(columns={ '01 !':'Gold','02 !':'Silver','03 !': 'Bronze',
                               '01 !.1':'Gold','02 !.1':'Silver','03 !.1': 'Bronze',
                               '01 !.2':'Gold','02 !.2':'Silver','03 !.2': 'Bronze',
                               'Total.1':'Total',
                             })
