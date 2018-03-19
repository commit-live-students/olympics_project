import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals

def q04_country_with_most_gold_medals(path):

    df = q03_summer_gold_medals(path)

    dfa = df.Gold
    total_gold = []

    for i in dfa.values:

        total_gold_medals = int(i[0]) + int(i[1]) + int(i[2])
        total_gold.append(total_gold_medals)

    dfa['total_gold'] = total_gold
    country_max_gold = dfa['total_gold'].idxmax()

    return country_max_gold

q04_country_with_most_gold_medals("data/olympics.csv")
