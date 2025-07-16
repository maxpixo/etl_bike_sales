import pandas as pd

def extract_csv(file_path: str) -> pd.DataFrame:

    # Reads a CSV file and returns a DataFrame

    try:
        df = pd.read_csv(file_path)
        print(f"############# Extracted {len(df)} rows from {file_path} #############")
        return df
    except Exception as e:
        print(f"Failed to extract data: {e}")
        raise