import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

  # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  x_predict = pd.Series([i for i in range(1880, 2051)])
  y_predict = slope * x_predict + intercept
  plt.plot(x_predict, y_predict, 'r')

  # Create second line of best fit
  recent_df = df[df['Year'] >= 2000]
  slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
  x_predict_recent = pd.Series([i for i in range(2000, 2051)])
  y_predict_recent = slope_recent * x_predict_recent + intercept_recent
  plt.plot(x_predict_recent, y_predict_recent, 'green')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
