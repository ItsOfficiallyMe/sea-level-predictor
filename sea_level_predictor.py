import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([year for year in range(1880, 2051)])
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r', label='Best fit line: 1880–2050')

    # Create second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series([year for year in range(2000, 2051)])
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    plt.plot(x_recent, y_recent, 'g', label='Best fit line: 2000–2050')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
