import pandas as pd
import io

def generate_burn_curve(df):
    df["Cumulative"] = df["Actual"].cumsum()
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    return df
