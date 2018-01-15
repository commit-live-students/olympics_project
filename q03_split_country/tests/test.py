import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q03_summer_gold_medals
from inspect import getargspec
import pandas

path = "data/olympics.csv"
df = q03_summer_gold_medals(path)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getargspec(q03_summer_gold_medals).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_return_shape(self):
        self.assertEqual(df.shape, (146, 15), "The Expected return shape does not match with the given return shape")
