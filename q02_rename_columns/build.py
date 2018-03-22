import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q01_load_data.build import q01_load_data
from pandas import Series
path = "data/olympics.csv"
df = pd.read_csv(path, header=0)
new_header = df.iloc[0]  # grab the first row for the header
new_header[0] = 'country name'
df = df[1:]  # take the data less the header row
df.columns = new_header  # set the header row as the df header
def q02_rename_columns(path):
    x = Series(df.columns)
    x[x.values == '01 !'] = 'Gold'
    x[x.values == '02 !'] = 'Silver'
    x[x.values == '03 !'] = 'Bronze'
    df.columns = x
    return(df)
print(q02_rename_columns(path).head(5))
