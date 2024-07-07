import unittest
from timeweave import generate_time_series
import pandas as pd

class TestGenerateTimeSeries(unittest.TestCase):

    def test_linear_trend(self):
        config = {
            "trend_type": "linear",
            "sub_option": None,
            "start_time": "2023-01-01",
            "num_points": 100,
            "granularity": "day",
            "data_range": [0, 100]
        }
        df = generate_time_series(**config)
        self.assertEqual(len(df), 100)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue("Date" in df.columns)
        self.assertTrue("Value" in df.columns)

if __name__ == "__main__":
    unittest.main()
