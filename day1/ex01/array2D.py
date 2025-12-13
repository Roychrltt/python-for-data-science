def slice_me(family: list, start: int, end: int) -> list:
    """Takes a 2D array, prints its shape, and returns a
        truncated version of the array based on the provided
        start and end arguments."""
    try:
        assert isinstance(family, list), "Input is not a list."
        assert all(isinstance(row, list) for row in family), \
            "Input is not a 2D list."
        assert all(len(row) == len(family[0]) for row in family), \
            "Lists are not of the same size"

        len1 = len(family)
        len2 = len(family[0])
        print(f"My shape is : ({len1}, {len2})")
        len4 = end
        if end < 0:
            len4 += len1
        len3 = len4 - start
        if len3 < 0:
            len3 = 0
        print(f"My new shape is : ({len3}, {len2})")
        s = slice(start, end)
        return family[s]

    except AssertionError as e:
        print("AssertionError:", e)
        return None
