import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals

def q05_difference_in_gold_medal(path):

    data = q03_summer_gold_medals(path)
    gold_data = data.Gold
    diff = []
    print(gold_data)
    for i in gold_data.values:

        diff.append(abs(int(i[0]) - int(i[1])))

    return max(diff)

q05_difference_in_gold_medal()
