import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    sea_level_plot = df.plot.scatter(x ='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = stats.linregress(x, y)

    extended_years = np.arange(x.min(), 2051)

    plt.plot(extended_years, res.intercept + res.slope*extended_years,'r', label='fitted line')

    # Create second line of best fit
    df_recent = df[df['Year'] > 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    res_recent = stats.linregress(x_recent, y_recent)
    restricted_years = np.arange(2000, 2051)
    restricted_sea_level = res_recent.intercept + res_recent.slope*restricted_years

    plt.plot(restricted_years, restricted_sea_level,'g', label='since 2000 line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()