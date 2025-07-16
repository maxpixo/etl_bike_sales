from sqlalchemy import create_engine
import pandas as pd
from etl_bike_sales.config.settings import DB_CONFIG

def get_engine():
    url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    engine = create_engine(url)
    return engine


def load(df: pd.DataFrame, table_name: str):
    # Loads Dataframe into a PostgresSQL Table.
    try:
        engine = get_engine()
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Loaded {len(df)} rows into PostgresSQL table {table_name}")

    except Exception as e:
        print(f"Error loading data into PostgresSQL table {table_name}: {e}")
        raise e