import unittest
import pandas as pd
from etl_bike_sales.transform.transformer import transform

class TestTransform(unittest.TestCase):
    def test_transform_removes_nulls(self):
        df = pd.DataFrame({
            "Date": ["2021-01-01", None],
            "Revenue": [100, None]
        })
        transformed = transform(df)
        self.assertEqual(len(transformed), 1)

    def test_transform_column_names(self):
        df = pd.DataFrame({" My Column ": [1], "Another Column": [2]})
        transformed = transform(df)
        self.assertIn("my_column", transformed.columns)
        self.assertIn("another_column", transformed.columns)

if __name__ == "__main__":
    unittest.main()
