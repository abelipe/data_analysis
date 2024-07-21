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
    print(monthly_mean_speed)

    print("Table of monthly wind mean speed", end="\n\n")
    monthly_table = table_from_historic(monthly)

    print("Plot of monthly wind mean speed per year", end="\n\n")
    plot_monthly_historic(monthly_table)


def plot_scatter_first_1000(model):
    pass

def plot_scatter_greatest_speed_1000(model):
    pass

def plot_histogram_speed(model):
    pass

def monthly_mean_speed(model):
    pass

def table_from_historic(monthly):
    pass

def plot_monthly_historic(monthly_table):
    pass


if __name__ == "__main__":
    main()

