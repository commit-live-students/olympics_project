# %load q04_country_with_most_gold_medals/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals

path = 'data/olympics.csv'


def q04_country_with_most_gold_medals(path):
    "write your solution here"
    df = q03_summer_gold_medals(path)
    return str(df.index[df.iloc[:,11] == max(df.iloc[:,11])][0])

q04_country_with_most_gold_medals(path)
