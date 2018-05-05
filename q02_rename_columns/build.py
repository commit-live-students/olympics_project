import pandas as pd
import numpy
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data

path = './data/olympics.csv'
def q02_rename_columns(path):
    df = q01_load_data(path)
    df = df.rename(columns={'01 !': 'Gold', '02 !':'Silver', '03 !':'Bronze'})
    return df
#q02_rename_columns(path)

