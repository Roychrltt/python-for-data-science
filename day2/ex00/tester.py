from load_csv import load


def main():
    """Main function to test function load_csv"""
    print(load("../life_expectancy_years.csv"))

    print("-------------------- Test case 1 --------------------")
    print(load("nonexist.csv"))

    print("-------------------- Test case 2 --------------------")
    print(load("load_csv.py"))


if __name__ == "__main__":
    main()
