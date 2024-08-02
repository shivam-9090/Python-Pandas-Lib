# Viewing the Data :
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.

# The head() method returns the headers and a specified number of rows, starting from the top.

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10)) # ==  print(df[:10])



# Print the first 5 rows of the DataFrame:

print(df.head()) #print only 5 rows



# There is also a tail() method for viewing the last rows of the DataFrame.

# The tail() method returns the headers and a specified number of rows, starting from the bottom.

print(df.tail())  #print last 5 rows



# Print information about the data:

print(df.info())  #all data print


# Null Values explantions :

# The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.