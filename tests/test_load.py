import unittest
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from etl_bike_sales.load.postgres_loader import load_with_psycopg2

load_dotenv()

class TestPostgresLoader(unittest.TestCase):
    def setUp(self):
        # Set up connection for cleanup
        self.conn = psycopg2.connect(
            dbname=os.getenv("PG_DB"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD"),
            host=os.getenv("PG_HOST"),
            port=os.getenv("PG_PORT")
        )
        self.cursor = self.conn.cursor()
        self.test_table = "test_bikes"

    def tearDown(self):
        # Drop the test table after test
        self.cursor.execute(f"DROP TABLE IF EXISTS {self.test_table};")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def test_load_with_psycopg2(self):
        # Sample data for test
        sample_data = {
            'date': ['2022-01-01', '2022-01-02'],
            'day': ['Saturday', 'Sunday'],
            'month': ['January', 'January'],
            'year': [2022, 2022],
            'customer_age': [30, 25],
            'age_group': ['Adult', 'Youth'],
            'customer_gender': ['M', 'F'],
            'country': ['USA', 'USA'],
            'state': ['CA', 'WA'],
            'product_category': ['Bikes', 'Bikes'],
            'sub_category': ['Mountain', 'Road'],
            'product': ['Bike A', 'Bike B'],
            'order_quantity': [1, 2],
            'unit_cost': [500.0, 450.0],
            'unit_price': [600.0, 550.0],
            'profit': [100.0, 200.0],
            'cost': [500.0, 900.0],
            'revenue': [600.0, 1100.0]
        }

        df = pd.DataFrame(sample_data)

        try:
            load_with_psycopg2(df, self.test_table)

            self.cursor.execute(f"SELECT COUNT(*) FROM {self.test_table};")
            count = self.cursor.fetchone()[0]

            self.assertEqual(count, 2)
            print(f"✅ Test table '{self.test_table}' inserted {count} rows successfully.")

        except Exception as e:
            self.fail(f"❌ Test failed with error: {e}")

if __name__ == "__main__":
    unittest.main()
