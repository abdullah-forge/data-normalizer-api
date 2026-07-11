import pandas as pd

def detect_column_schema(df):
    schema = {}

    for col in df.columns:
        col_data = df[col]
        if pd.api.types.is_datetime64_any_dtype(col_data):
            schema[col] = "datetime"
        elif pd.api.types.is_numeric_dtype(col_data):
            if col_data.isnull().any() or not (col_data.dropna() == col_data.dropna().astype(int)).all():
                schema[col] = "float"
            else:
                schema[col] = "int"
        else:
            try:
                pd.to_datetime(col_data.dropna().head(10), errors='raise')
                schema[col] = "datetime"
            except (ValueError, TypeError):
                schema[col] = "string"
    return schema
