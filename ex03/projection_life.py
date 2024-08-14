import numpy as np
from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def change(param: int, pos=None):
    param = int(param)
    if param >= 1e3:
        param /= 1e3
        param = f"{int(param)}k"
    return param


def projection_life(income_csv: str, life_csv: str):
    try:
        if (income_csv.__class__ != str
            or life_csv.__class__ != str):
            raise Exception("Invalid Arguments")
        income_data = load(income_csv)
        life_data = load(life_csv)
        if income_data is None or life_data is None:
            raise Exception("Couldn't load datasets")
        income_1900 = income_data['1900']
        life_1900 = life_data['1900']
        income_shape = np.array(income_1900.shape)
        life_shape = np.array(life_1900.shape)
        if income_shape.ndim != 1 or life_shape.ndim != 1 or \
            income_shape[0] != life_shape[0]:
            raise Exception("Invalid datashape")
        
        # plt.figure(figsize=(10, 6))
        plt.scatter(income_1900, life_1900)
        plt.xscale('log')
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title(1900)
        plt.gca().xaxis.set_major_formatter(FuncFormatter(change))
        
        plt.show()
    except Exception as e:
        print(f"An Error occurs: {e}")
        return None

def main():
    projection_life("income_per_person_gdppercapita_ppp_inflation_adjusted.csv", "life_expectancy_years.csv")
    return 1


if __name__ == "__main__":
    main()