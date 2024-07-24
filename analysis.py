# Analysis of wind data
import os
import pandas as pd
import matplotlib.pyplot as plt

RESULTS_DIR = "Results"

def main():
    print("Loading data...", end="\n\n")
    model = read_model("Data/model.txt")

    try:
        os.mkdir(RESULTS_DIR)
    except FileExistsError:
        pass

    print("Scatter figures matrix of first 1000 records", end="\n\n")
    plot_scatter_first_1000(model)

    print("Scatter figures matrix of first 1000 records"
          " with greatest wind speed", end="\n\n")
    plot_scatter_greatest_speed_1000(model)

    print("Histogram of wind speed with 36 partitions", end="\n\n")
    plot_histogram_speed(model)

    print("Monthly historic of wind mean speed", end="\n\n")
    monthly = monthly_mean_speed(model)

    print("Table of monthly wind mean speed", end="\n\n")
    monthly_table = table_from_historic(monthly)

    print("Plot of monthly wind mean speed per year", end="\n\n")
    plot_monthly_historic(monthly_table)


def plot_scatter_first_1000(model):
    # Select the first 1000 rows for "Speed(m/s)" and "Direction(deg)"
    subset = model.iloc[:1000]
    speed = subset["Speed(m/s)"]
    direction = subset["Direction(deg)"]
    
    # Create a scatter plot
    plt.scatter(speed, direction, alpha=0.2)
    plt.xlabel("Speed(m/s)")
    plt.ylabel("Direction(deg)")
    plt.title("Scatter Plot of the First 1000 Records")
    plt.show()

def plot_scatter_greatest_speed_1000(model):
    # Select the top 1000 rows with the greatest "Speed(m/s)"
    top_speeds = model.nlargest(1000, "Speed(m/s)")
    
    # Assuming "Direction(deg)" is the column to plot against "Speed(m/s)"
    plt.scatter(top_speeds["Speed(m/s)"], top_speeds["Direction(deg)"], alpha=0.2)
    plt.xlabel("Speed(m/s)")
    plt.ylabel("Direction(deg)")
    plt.title("Scatter Plot of the Top 1000 Speeds")
    plt.show()

def plot_histogram_speed(model):
    # Plotting the histogram with 36 bins
    plt.hist(model["Speed(m/s)"], bins=36, alpha=0.75, edgecolor='black')
    
    # Adding labels and title
    plt.xlabel("Speed(m/s)")
    plt.ylabel("Frequency")
    plt.title("Histogram of Wind Speeds")
    
    # Display the plot
    plt.show()

def monthly_mean_speed(model):
    monthly = model["Speed(m/s)"].groupby([model.index.year,
                                           model.index.month]).mean()
    monthly.rename_axis(index=["Year", "Month"], inplace=True)
    print(monthly, end="\n\n")
    monthly.to_csv(RESULTS_DIR + "/mon_hist_wind_mean_speed.txt", "\t")
    monthly.plot(legend=True, figsize=(15, 5))
    plt.show()
    return monthly

def table_from_historic(monthly):
    # Debugging: Print available columns in the DataFrame
    print("Columns in DataFrame:", monthly.columns)

    if isinstance(monthly.index, pd.MultiIndex):
        # Assuming datetime information is in a specific level, e.g., level 0
        datetime_index = pd.to_datetime(monthly.index.get_level_values(0))
        monthly['Year'] = datetime_index.year
        monthly['Month'] = datetime_index.month
    else:
        # Convert the index to a DateTimeIndex if it's not already one
        monthly.index = pd.to_datetime(monthly.index)
        monthly['Year'] = monthly.index.year
        monthly['Month'] = monthly.index.month
    
    # Group by year and month, then calculate mean velocity
    # Ensure 'Speed(m/s)' column exists
    if 'Speed(m/s)' in monthly.columns:
        monthly_mean = monthly.groupby(['Year', 'Month'])['Speed(m/s)'].mean().reset_index()
    else:
        raise KeyError("Column not found: 'Speed(m/s)'")
    
    # Pivot table to have years as rows and months as columns
    pivot_table = monthly_mean.pivot(index='Year', columns='Month', values='Speed(m/s)')
    
    return pivot_table


def plot_monthly_historic(monthly_table):
    # Assuming 'monthly_table' needs to be adjusted to match your description
    # This step might be redundant or need adjustment based on the actual structure of 'monthly_table'
    # The following line is an example based on your description and might need to be adapted
    monthly_table = monthly_table.reset_index().pivot(index='Year', columns='Month', values='Speed(m/s)').T
    
    # Plotting
    monthly_table.loc['Speed(m/s)'].plot(figsize=(15, 5), legend=False)
    plt.xlabel("Year")
    plt.ylabel("Mean Wind Speed (m/s)")
    plt.title("Monthly Mean Wind Speed per Year")
    plt.show()

def read_model(path):
    model = pd.read_csv(path, sep="\s+", skiprows=3,
                        usecols=["YYYYMMDD", "HHMM", "M(m/s)", "D(deg)"],
                        parse_dates={"Timestamp": [0, 1]}, index_col="Timestamp")
    model.rename(columns={"M(m/s)": "Speed(m/s)",
                          "D(deg)": "Direction(deg)"},
                 inplace=True)
    return model

if __name__ == "__main__":
    main()

