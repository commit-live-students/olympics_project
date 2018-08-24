# %load q02_rename_columns/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

def q02_rename_columns(path):
    'write your solution here'
    df = q01_load_data(path)
    df.columns = ['country name', '# Summer', 'Gold', 'Silver', 'Bronze', 'Total', '# Winter', 'Gold', 'Silver', 'Bronze','Total', '# Games', 'Gold', 'Silver', 'Bronze', 'Combined total']
    return df



