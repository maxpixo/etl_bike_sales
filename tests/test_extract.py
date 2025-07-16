import unittest
import pandas as pd
from etl_bike_sales.extract.csv_extractor import extract_csv

class TestExtract(unittest.TestCase):
    def test_extract_csv(self):
        df = extract_csv("data/raw/Sales.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)

if __name__ == "__main__":
    unittest.main()
