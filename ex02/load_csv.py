import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """Load dataset of dimensions"""
    try:
        df = pd.read_csv(path)
        rows, cols = df.shape
        print(f"Loading dataset of dimensions ({rows}, {cols})")
        return df
    except Exception as e:
        print(f"An Error occurs: {e}")
        return None
