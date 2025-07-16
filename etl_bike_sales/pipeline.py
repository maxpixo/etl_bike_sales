from etl_bike_sales.extract.csv_extractor import extract_csv
from etl_bike_sales.transform.transformer import transform
from etl_bike_sales.load.postgres_loader import load_with_psycopg2




def run_pipeline(filepath: str, table_name: str):
    print(f"######## Starting ETL Pipeline...")
    df = extract_csv(filepath)
    df_transformed = transform(df)
    load_with_psycopg2(df_transformed, table_name)
    print(f"ETL Pipeline completed successfully")