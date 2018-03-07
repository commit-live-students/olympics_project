import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals

path="./data/olympics.csv"
def q04_country_with_most_gold_medals(path):
    "write your solution here"
    df = q03_summer_gold_medals(path)
    gold_count = df.iloc[:,1].sort_values(ascending=False)
    max_gold_count = gold_count[:1].index
    country_name = max_gold_count[0]
    country_with_most_gold_medals = country_name.replace('\xc2\xa0',"")
    return country_with_most_gold_medals
    
