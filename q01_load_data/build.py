# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def q01_load_data(path):
   
    data=pd.read_csv(path,header=1,sep=',')
    df=data.rename(columns={'Unnamed: 0':'country name'})
    return(df)
    # use .read_csv function to read the
    # data and header=0 to skip the first row


