from load_csv import load
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd


def parse_population(val):
    """Safely converts strings end with M or k to floats."""
    if pd.isna(val):
        return 0.0
    val = str(val).lower()
    if 'm' in val:
        return float(val.replace('m', '')) * 1_000_000
    if 'k' in val:
        return float(val.replace('k', '')) * 1_000
    try:
        return float(val)
    except ValueError:
        return None


def main():
    """Main function to load data from file and display the life expectancy of
       France population using Matplotlib"""
    df = load("../population_total.csv")
    campus_country = "France"
    other_country = "Belgium"

    if len(sys.argv) > 2:
        campus_country = sys.argv[1]
        other_country = sys.argv[2]

    for c in [campus_country, other_country]:
        if c not in df.index:
            print(f"Error: The country '{c}' was not found in the dataset.")
            sys.exit(1)

    plt.figure()
    for country in [campus_country, other_country]:
        data = df.loc[country]
        years = data.index.astype(int)

        values = data.apply(parse_population)
        mask = (years >= 1800) & (years <= 2050)
        current_color = "green" if country == "France" else "tab:blue"
        plt.plot(years[mask], values[mask], label=country, color=current_color)


    plt.ticklabel_format(style='plain', axis='y')
    def format_millions(x, pos):
        return f'{int(x/1e6)}M'
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_millions))

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc='lower right')
    plt.xticks(range(1800, 2051, 40))

    plt.show()


if __name__ == "__main__":
    main()
