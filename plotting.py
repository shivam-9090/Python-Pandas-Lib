# Plotting :
# Pandas uses the plot() method to create diagrams.

# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

# Scatter Plot :
# Specify that you want a scatter plot with the kind argument:

# kind = 'scatter'

# A scatter plot needs an x- and a y-axis.

# In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.

# Include the x and y arguments like this:

# x = 'Duration', y = 'Calories'

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

# Histogram :

# Use the kind argument to specify that you want a histogram:

# kind = 'hist'

# A histogram needs only one column.

# A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?

df["Duration"].plot(kind = 'hist')

# Note: The histogram tells us that there were over 100 workouts that lasted between 50 and 60 minutes.