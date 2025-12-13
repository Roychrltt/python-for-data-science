#!/usr/bin/python3

from give_bmi import give_bmi, apply_limit


def main():
    """The main function to test function give_bmi and apply_limit."""

    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    # Error handling
    print("\n-------------------- Test case 1: height type error --------------------:")
    give_bmi([1, 2, 8, 3.4, "a"], [1, 2, 3, 4, 5])

    print("\n-------------------- Test case 2: weight type error --------------------:")
    give_bmi([1, 2, 8, 3.4, 5.6], ["a", 2, 3, 4, 5])

    print("\n-------------------- Test case 3: negative or 0 --------------------:")
    give_bmi([1, 2, 8, 3.4, -1], [1, 2, 3, 4, 5])
    give_bmi([1, 2, 8, 3.4, 1], [0, 2, 3, 4, 5])

    print("\n-------------------- Test case 4: lists' size not equal --------------------:")
    give_bmi([1, 2, 8, 3.4, 1], [1, 2, 3, 4, 5, 8, 9])

    print("\n-------------------- Test case 5: bmi type error --------------------:")
    apply_limit([1, 2, 3, 1, "a"], 2)

    print("\n-------------------- Test case 6: limit is not an integer --------------------:")
    apply_limit([1, 2, 3, 1, 5], 2.3)


if __name__ == "__main__":
    main()
