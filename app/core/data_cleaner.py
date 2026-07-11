import pandas as pd
import numpy as np

def clean_data(df, schema):
    df = df.copy()
    for col in df.columns:
        dtype = schema.get(col)
        if dtype == "int":
            numeric_series = pd.to_numeric(df[col], errors='coerce')
            df[col] = numeric_series.astype('Int64')
        elif dtype == "float":
            df[col] = pd.to_numeric(df[col], errors='coerce')
        elif dtype == "string":
            df[col] = df[col].astype(str).str.strip().replace('', np.nan)
    return df

