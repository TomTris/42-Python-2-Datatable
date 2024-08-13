import matplotlib.pyplot as plt
from load_csv import load


def plot_country_life_expectancy(country_name1: str, country_name2: str, csv_path: str):
    try:
        df = load(csv_path)
        if df is None:
            return None
        country_data1 = df[df['country'] == country_name1]
        country_data2 = df[df['country'] == country_name2]
        if country_data1.empty:
            print(f"No data found for {country_name1}")
            return None
        if country_data2.empty:
            print(f"No data found for {country_name2}")
            return None
        years1 = country_data1.columns[1:251].astype(int)
        years2 = country_data2.columns[1:251].astype(int)
        life_expectancy1 = country_data1.iloc[0, 1:251].values
        life_expectancy2 = country_data2.iloc[0, 1:251].values
    except Exception as e:
        print(f"An Error occurs: {e}")
        return None
    plt.figure(figsize=(10, 6))
    plt.plot(years1, life_expectancy1, color='g', label=country_name1)
    plt.plot(years2, life_expectancy2, color='b', label=country_name2)
    plt.xlabel("Year")
    plt.ylabel("life_expectancy")
    plt.title(f"Life expectancy over time for {country_name1} and {country_name2}")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    return 1


if __name__ == "__main__":
    main()
