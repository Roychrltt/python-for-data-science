import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """Takes a path as argument, writes the dimensions of the data set
       and returns it"""
    try:
        assert isinstance(path, str), "Path is not a string."
        assert os.path.exists(path), "File does not exist."
        assert path.endswith(".csv"), "Not a csv file."
        dataset = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions:", dataset.shape)
        return dataset

    except AssertionError as e:
        print("AssertionError:", e)
        return None

    except Exception as e:
        print("Unexpected error:", e)
        return None
