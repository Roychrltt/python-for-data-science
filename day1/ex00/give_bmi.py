import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Takes 2 lists (heights and weights) of int or float and returns\
        a list of BMI values."""
    try:
        assert isinstance(height, list), "Input is not a list."
        assert isinstance(weight, list), "Input is not a list."
        assert any(h <= 0 for h in height),\
                "Heights must all be positive values"
        assert any(w <= 0 for w in weight),\
                "Weights must all be positive values"
        assert all(isinstance(h, int | float) for h in height),\
                "Heights must all be int ot float."
        assert all(isinstance(w, int | float) for w in weight),\
                "Weights must all be int ot float."
        assert (len(height) == len(weight)), "Two lists' size not equal."

        h = np.array(height, dtype = float)
        w = np.array(weight, dtype = float)
        return (w / h ** 2).tolist()

    except AssertionError as e:
        print("AssertionError:", e)
        return None

    except Exception as e:
        raise


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Takes a list of int or float and an integer limit.
        Returns a list of bools, True if value is above the limit."""
    try:
        assert isinstance(bmi, list), "Input is not a list."
        assert isinstance(limit, int), "Limit is not an int."
        assert all(isinstance(i, int | float) for i in bmi),\
                "BMIs must all be int ot float."
        return [i > limit for i in bmi]

    except AssertionError as e:
        print("AssertionError:", e)
        return None

    except Exception as e:
        raise
