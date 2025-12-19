from load_csv import load
import matplotlib.pyplot as plt
import numpy as np
import sys


def main():
    """Main function to load data from file and display the life expectancy of
       the population of France and another country using Matplotlib"""
    df = load("../population_total.csv")
    if df is None:
        sys.exit(1)

    france = df.loc["France"]
    print(france)
    belgium = df.loc["Belgium"]
    years = france.index.astype(int)

    plt.figure()
    plt.plot(years, france, label="France", color="#159f3f")
    plt.plot(years, belgium, label="Belgium", color="#5d6fe5")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    x = np.arange(1800, 2050, 40)
    y = np.arange(0, 7e7, 2e7)
    plt.yticks(y)
    plt.xticks(x)
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()
