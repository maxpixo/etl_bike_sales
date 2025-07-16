from etl_bike_sales.pipeline import run_pipeline


if __name__ == "__main__":
    csv_path = "data/raw/Sales.csv"
    table_name = "bikes"
    run_pipeline(csv_path, table_name)
