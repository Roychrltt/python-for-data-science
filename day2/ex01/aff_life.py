from load_csv import load
import matplotlib.pyplot as plt
import sys


def main():
    """Main function to load data from file and display the life expectancy of
       France population using Matplotlib"""
    df = load("../life_expectancy_years.csv")
    if df is None:
        sys.exit(1)
    france = df.loc["France"]
    years = france.index.astype(int)
    plt.figure()
    plt.plot(years, france.values)
    plt.title("France Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    xticks = [year for year in years if (year - 1800) % 40 == 0]
    plt.xticks(xticks)
    plt.show()


if __name__ == "__main__":
    main()
