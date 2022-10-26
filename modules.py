# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Define URL of the files to variables
filename_test = 'data/test.csv'

# Read in csv files and transform then to dataframes
df = pd.read_csv(filename_test)

# Define x and y values
x_values = list[df['x']]
y_values = list[df['y']]

# Plot scatter plot
df.plot.scatter(x_values, y_values)
plt.show()