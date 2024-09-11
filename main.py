import pandas as pd
import matplotlib.pyplot as plt


def load_data(url):
    data = pd.read_csv(url)
    return data


def generate_descriptive_statistics(data):
    des_stat = data.describe()
    return des_stat


def generate_summary_statistics(filter_data):
    summary_stat = {
        "mean": filter_data.mean(),
        "median": filter_data.median(),
        "std": filter_data.std(),
    }
    return summary_stat


def main():
    url = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
    df = load_data(url)
    df_filtered = df[
        [
            "Mortality rate, infant (per 1,000 live births)",
            "GDP per capita (constant 2010 US$)",
        ]
    ]
    # 1 descriptive statistics
    des_stat = generate_descriptive_statistics(df_filtered)
    print("Descriptive Statistics:\n", des_stat)

    # 2 summary statistics
    summary_stat = generate_summary_statistics(df_filtered)
    print("\nSummary Statistics:\n", summary_stat)

    # 3 Visualization
    df_filtered.plot.scatter(
        x="GDP per capita (constant 2010 US$)",
        y="Mortality rate, infant (per 1,000 live births)",
        title="Infant Mortality Against GDP per Capita",
    )
    print("\nVisualization:\n")
    plt.show()


if __name__ == "__main__":
    main()
