
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# import sys
# import os
#
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals

path = 'data/olympics.csv'
def q04_country_with_most_gold_medals(path):
    'write your solution here'
    df = q03_summer_gold_medals(path)
    df['Gold Total'] = df[['Gold']].astype(int).sum(1) #Create a column for the Gold Total
    maxGold = df['Gold Total'].idxmax() # get the max of the gold total
    df.drop(['Gold Total'], axis=1) #drop the column Gold Total
    return maxGold #return the string Country name

print(q04_country_with_most_gold_medals(path))


