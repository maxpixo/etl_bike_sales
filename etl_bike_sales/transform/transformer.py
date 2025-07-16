import pandas as pd


def clean_column_names(df):
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:

    try:
        df = df.dropna()
        df = clean_column_names(df)

        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')

        print(f"Transformed DataFrame with {df.shape[0]} rows and {df.shape[1]} columns")
        return df
    except Exception as e:
        print(f"Failed to transform data: {e}")
        raise