import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def load_with_psycopg2(df: pd.DataFrame, table_name: str):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname=os.getenv("PG_DB"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD"),
            host=os.getenv("PG_HOST"),
            port=os.getenv("PG_PORT")
        )
        cursor = conn.cursor()

        # Create table (if not exists)
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            date DATE,
            day TEXT,
            month TEXT,
            year INT,
            customer_age INT,
            age_group TEXT,
            customer_gender TEXT,
            country TEXT,
            state TEXT,
            product_category TEXT,
            sub_category TEXT,
            product TEXT,
            order_quantity INT,
            unit_cost FLOAT,
            unit_price FLOAT,
            profit FLOAT,
            cost FLOAT,
            revenue FLOAT
        );
        """
        cursor.execute(create_table_query)

        # Insert data row-by-row
        for _, row in df.iterrows():
            cursor.execute(
                f"""
                INSERT INTO {table_name} (
                    date, day, month, year,
                    customer_age, age_group, customer_gender,
                    country, state, product_category, sub_category, product,
                    order_quantity, unit_cost, unit_price, profit, cost, revenue
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    row['date'], row['day'], row['month'], row['year'],
                    row['customer_age'], row['age_group'], row['customer_gender'],
                    row['country'], row['state'], row['product_category'], row['sub_category'], row['product'],
                    row['order_quantity'], row['unit_cost'], row['unit_price'], row['profit'],
                    row['cost'], row['revenue']
                )
            )

        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ Inserted {len(df)} rows into table '{table_name}'")

    except Exception as e:
        print(f"❌ Error loading data into PostgreSQL: {e}")
