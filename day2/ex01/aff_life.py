from load_csv import load
import matplotlib.pyplot as plt
import sys


def main():
    """Main function to load data from file and display the life expectancy of
       France population using Matplotlib"""
    df = load("../life_expectancy_years.csv")
    if df is None:
        sys.exit(1)
    # print(sorted(df.index))
    country = "France"

    if len(sys.argv) > 1:
        country = sys.argv[1]

    if country not in df.index:
        print(f"Error: The country '{country}' was not found in the dataset.")
        sys.exit(1)

    life = df.loc[country]
    years = life.index.astype(int)
    plt.figure()
    plt.plot(years, life.values)
    titre = country + " Life Expectancy Projections"
    plt.title(titre)
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    xticks = [year for year in years if (year - 1800) % 40 == 0]
    plt.xticks(xticks)
    plt.show()


if __name__ == "__main__":
    main()
