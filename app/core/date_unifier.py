import pandas as pd

def unify_dates(df, schema):
    df = df.copy()
    for col, dtype in schema.items():
        if dtype == "datetime" and col in df.columns:
            datetime_series = pd.to_datetime(df[col], errors= 'coerce')
            df[col] = datetime_series.dt.strftime('%Y-%m-%d %H:%M:%S')
    return df
