import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q05_difference_in_gold_medal
from inspect import getargspec
import pandas

path = "data/olympics.csv"
df = q05_difference_in_gold_medal(path)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getargspec(q05_difference_in_gold_medal).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_output_type(self):
        self.assertEqual(df, 147, "The Expected return type does not match the return type")
