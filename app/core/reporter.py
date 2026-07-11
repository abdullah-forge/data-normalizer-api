import pandas as pd

def generate_report(original_df, cleaned_df, schema):
    report = {}
    report["total_rows"] = len(cleaned_df)
    report["total_columns"] = len(cleaned_df.columns)
    report["total_nulls_found"] = int(cleaned_df.isnull().sum().sum())
    report["schema"] = schema
    original_nulls = int(original_df.isnull().sum().sum())
    report["coerced_invalid_values"] = report["total_nulls_found"] - original_nulls
    return report
