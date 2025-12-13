#!/usr/bin/python3

from array2D import slice_me


def main():
    """The main function to test function slice_me"""

    family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    # Error handling
    print("\n-------------------- Test case 1: input is not a 2D array --------------------:")
    ll = [1, 2, 3, 4]
    print(slice_me(ll, 0, 3))

    print("\n-------------------- Test case 2: input lists are not of the same size--------------------:")
    lll = [[1, 2, 3], [1, 2, 3, 4], [1, 2, 3]]
    print(slice_me(ll, 0, 3))

    print("\n-------------------- Test case 3: out of range --------------------:")
    print(slice_me(family, 0, -10))
    print(slice_me(family, 7, -10))
    

if __name__ == "__main__":
    main()
