import matplotlib.pyplot as plt
from load_csv import load


def plot_country_life_expectancy(country_name: str, csv_path: str):
    """Display plot about life expectancy of a country"""
    try:
        df = load(csv_path)

        if df is None:
            return None
        country_data = df[df['country'] == country_name]

        if country_data.empty:
            print(f"No data found for {country_name}")
            return None

        years = country_data.columns[1:].astype(int)
        life_expectancy = country_data.iloc[0, 1:].values
    except Exception as e:
        print(f"An Error occurs: {e}")
        return None

    plt.figure(figsize=(10, 6))
    plt.plot(years, life_expectancy, color='b', label=country_name)
    plt.xlabel("Year")
    plt.ylabel("life_expectancy")
    plt.title(f"Life expectancy over time for {country_name}")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    return 1


if __name__ == "__main__":
    main()
