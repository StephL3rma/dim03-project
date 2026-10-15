import sys
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame.

    Args:
        path: Relative path to the CSV file.

    Returns:
        The loaded data.
    """
    return pd.read_csv(path, sep=",", encoding="utf-8-sig")


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows from a DataFrame.

    Args:
        df: The data to clean.

    Returns:
        The data without duplicate rows, with a fresh 0..n-1 index. 
    """
    return df.drop_duplicates().reset_index(drop=True) 


if __name__ == "__main__":
    print(load_data(sys.argv[1]).head())
