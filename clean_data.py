# Data Cleaning
# Data cleaning means fixing bad data in your data set.

# Bad data could be:

# ->Empty cells
# ->Data in wrong format
# ->Wrong data
# ->Duplicates
# In this tutorial you will learn how to deal with all of them.

# -> Empty Cells :
# Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows
# One way to deal with empty cells is to remove rows that contain empty cells.

# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna() 
# The dropna() method is a method in pandas, a Python library for data manipulation and analysis. It is used to drop rows or columns that contain missing or NaN (Not a Number) values.
# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
print(new_df.to_string())

# If you want to change the original DataFrame, use the inplace = True argument:

df.dropna(inplace = True)

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.


# Replace Empty Values :

# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:

df.fillna(130, inplace = True)

#Replace Only For Specified Columns :

# The example above replaces all empty cells in the whole Data Frame.
# To only replace empty values for one column, specify the column name for the DataFrame:

df["Calories"].fillna(130, inplace = True)

# Replace Using Mean, Median, or Mode :

# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
# Mean = the average value (the sum of all values divided by number of values).

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)
# Median = the value in the middle, after you have sorted all values ascending. (the middle value)

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)
# Mode = the value that appears most frequently. (means most use values)



# Data of Wrong Format :

# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())






# Wrong Data :

# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

# Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

# If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.

# It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.



# Replacing Values :

# One way to fix wrong values is to replace them with something else.

# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:

df.loc[7, 'Duration'] = 45 
# In data 7 line will be a change and the duration will be 45 minutes.
# and loc = location.

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.

# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

# Loop through all values in the "Duration" column.

# If the value is higher than 120, set it to 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

# Removing Rows :

# Another way of handling wrong data is to remove the rows that contains wrong data.

# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.

# Delete rows where "Duration" is higher than 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

# Discovering Duplicates :

# Duplicate rows are rows that have been registered more than one time.

# To discover duplicates, we can use the duplicated() method.

# The duplicated() method returns a Boolean values for each row:

# Returns True for every row that is a duplicate, otherwise False:

print(df.duplicated())

# Removing Duplicates :

# To remove duplicates, use the drop_duplicates() method.

df.drop_duplicates(inplace = True)

# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.