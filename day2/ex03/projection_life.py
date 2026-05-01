import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def parse_value(val):
    """Safely converts strings end with M or k to floats."""
    if pd.isna(val):
        return None
    val = str(val).lower()
    if 'k' in val:
        return float(val.replace('k', '')) * 1_000
    if 'm' in val:
        return float(val.replace('m', '')) * 1_000_000
    try:
        return float(val)
    except ValueError:
        return None


def main():
    income_df = load("../gdp.csv")
    life_df = load("../life_expectancy_years.csv")

    if income_df is None or life_df is None:
        return

    income_1900 = income_df['1900'].apply(parse_value)
    life_1900 = life_df['1900'].apply(parse_value)

    merged = pd.concat([income_1900, life_1900], axis=1, join='inner')
    merged.columns = ['GDP', 'LifeExpectancy']
    merged = merged.dropna()

    plt.figure(figsize=(10, 7))
    plt.scatter(merged['GDP'], merged['LifeExpectancy'], label='Country Data')

    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
