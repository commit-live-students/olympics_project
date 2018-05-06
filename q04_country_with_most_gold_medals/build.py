# %load q04_country_with_most_gold_medals/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals


def q04_country_with_most_gold_medals(path):
    'write your solution here'
    df = q03_summer_gold_medals(path)
    pd = df['Gold'].sum(axis=1).max() ==df['Gold'].sum(axis=1)
    country = df[pd].index[0][:-1]
    return country

q04_country_with_most_gold_medals('data/olympics.csv')

