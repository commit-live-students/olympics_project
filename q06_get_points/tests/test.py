import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q06_get_points
from inspect import getargspec

import pandas

path = "data/olympics.csv"
df = q06_get_points(path)
values = list(df[:10].values)
check = list([4, 54, 260, 32, 44, 1846, 1138, 86, 48, 2])


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getargspec(q06_get_points).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_instance(self):
        self.assertIsInstance(df, pandas.Series, "The Expected return type does not match with the given")

    def test_return(self):
        self.assertListEqual(values, check, "The Expected return does not match the output")
