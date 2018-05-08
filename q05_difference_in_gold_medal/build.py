# %load q05_difference_in_gold_medal/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals

path = './data/olympics.csv'
def q05_difference_in_gold_medal(path):
    df = q03_summer_gold_medals(path)
    return (df.iloc[:,1].astype(np.int) - df.iloc[:,6].astype(np.int)).max()
    
    #   'write your solution here'
    

q05_difference_in_gold_medal(path)



