# Analysis of wind data
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Loading data...", end="\n\n")
    model = read_model("Data/model.txt")

    print("Scatter figures matrix of first 1000 records", end="\n\n")
    plot_scatter_first_1000(model)

    print("Scatter figures matrix of first 1000 records"
          " with greatest wind speed", end="\n\n")
    plot_scatter_greatest_speed_1000(model)

    print("Histogram of wind speed with 36 partitions", end="\n\n")
    plot_histogram_speed(model)

    print("Monthly historic of wind mean speed", end="\n\n")
    monthly = monthly_mean_speed(model)
    print(monthly, end="\n\n")

    print("Table of monthly wind mean speed", end="\n\n")
    monthly_table = table_from_historic(monthly)

    print("Plot of monthly wind mean speed per year", end="\n\n")
    plot_monthly_historic(monthly_table)


def plot_scatter_first_1000(model):
    pass

def plot_scatter_greatest_speed_1000(model):
    pd.plotting.scatter_matrix(model.nlargest(1000, "Speed(m/s)"))
    plt.show()

def plot_histogram_speed(model):
    pass

def monthly_mean_speed(model):
    monthly = model["Speed(m/s)"].groupby([model.index.year,
                                           model.index.month]).mean()
    monthly.rename_axis(index=["Year", "Month"], inplace=True)
    return monthly

def table_from_historic(monthly):
    pass

def plot_monthly_historic(monthly_table):
    pass

def read_model(path):
    model = pd.read_csv(path, "\s+", skiprows=3,
                        usecols=["YYYYMMDD", "HHMM", "M(m/s)", "D(deg)"],
                        parse_dates={"Timestamp": [0, 1]}, index_col="Timestamp")
    model = model
    model.rename(columns={"M(m/s)": "Speed(m/s)",
                          "D(deg)": "Direction(deg)"},
                 inplace=True)
    return model

if __name__ == "__main__":
    main()

