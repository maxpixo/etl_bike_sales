import unittest
from sqlalchemy import create_engine
from etl_bike_sales.config.settings import DB_CONFIG

class TestPostgresConnection(unittest.TestCase):
    def test_connection(self):
        """
        Test if we can successfully connect to the PostgreSQL database.
        """
        try:
            engine = create_engine(
                f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
                f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
            )
            with engine.connect() as conn:
                result = conn.execute("SELECT 1")
                self.assertEqual(result.scalar(), 1)
                print("✅ Connected to PostgreSQL successfully.")
        except Exception as e:
            self.fail(f"❌ PostgreSQL connection failed: {e}")

if __name__ == "__main__":
    unittest.main()
