import matplotlib.pyplot as plt
from load_csv import load


def best_function(index):
    """Change form character-form to number-from"""
    m = 1
    if index[-1] == 'M':
        m = 1e6
    if index[-1] == 'k':
        m = 1e3
    if index[-1] == 'B':
        m = 1e9
    if m != 1:
        index = index[:-1]
    return float(index) * m


def population_between_2_country(country_name1: str,
                                 country_name2: str, csv_path: str):
    """Display difference between population of 2 country"""
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
        years1 = country_data1.columns[1:251].astype(float)
        years2 = country_data2.columns[1:251].astype(float)
        life_expectancy1 = country_data1.values[0, 1:251]
        life_expectancy2 = country_data2.values[0, 1:251]
        life1 = [best_function(e) for e in life_expectancy1]
        life2 = [best_function(e) for e in life_expectancy2]
    except Exception as e:
        print(f"An Error occurs: {e}")
        return None
    plt.figure(figsize=(10, 6))
    plt.plot(years1, life1, color='g', label=country_name1)
    plt.plot(years2, life2, color='b', label=country_name2)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title(f"Population over time for {country_name1} and {country_name2}")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    return 1


if __name__ == "__main__":
    main()
