#!/usr/bin/env python
# coding: utf-8

# # question 01

# In[9]:


import pandas as pd
course_name = ['datascience', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]
df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})
print(df.iloc[1])


# # question 02

Q2. What is the difference between the functions loc and iloc in pandas.DataFrame?

loc and iloc are two functions in pandas that are used to select subsets of a DataFrame based on the labels or integer indexes of the rows and columns. The main difference between the two functions is in how they specify the row and column indexes.

loc selects rows and columns based on their labels. This means that you need to provide the row and column labels or boolean arrays of the same length as the DataFrame. For example, df.loc[1:3, ['A', 'B']] will select rows with labels 1, 2, and 3, and columns with labels 'A' and 'B'.

iloc selects rows and columns based on their integer positions. This means that you need to provide the row and column positions as integers or boolean arrays of the same length as the DataFrame. For example, df.iloc[1:3, [0, 1]] will select rows with integer positions 1 and 2, and columns with integer positions 0 and 1.

In summary, loc uses labels to select rows and columns, while iloc uses integer positions
# # question 03

# In[11]:


import pandas as pd
import numpy as np

columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]

# Creating a DataFrame
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)

# Reindexing the DataFrame
reindex = [3, 0, 1, 2]
new_df = df1.reindex(reindex)

# Finding the output for both new_df.loc[2] and new_df.iloc[2]
print(new_df.loc[2])
print(new_df.iloc[2])


# # question 04
Write a code to find the following statistical measurements for the above dataframe df1:
(i) mean of each and every column present in the dataframe.
(ii) standard deviation of column, ‘column_2’

Here's the code to find the mean of each column and the standard deviation of the 'column_2' in the DataFrame df1:
# In[13]:


import pandas as pd
import numpy as np

columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1, 2, 3, 4, 5, 6]

#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)

# (i) Mean of each column
print("Mean of each column:\n", df1.mean())

# (ii) Standard deviation of 'column_2'
print("\nStandard deviation of 'column_2':\n", df1['column_2'].std())


# # question 05
Replace the data present in the second row of column, ‘column_2’ by a string variable then find the
mean of column, column_2.
If you are getting errors in executing it then explain why.
[Hint: To replace the data use df1.loc[] and equate this to string data of your choice.]

To replace the data present in the second row of the 'column_2' in the DataFrame df1 by a string variable, and then find the mean of the column, we can use the following code:
# In[14]:


import pandas as pd
import numpy as np

columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1, 2, 3, 4, 5, 6]

#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)

# Replace the data in the second row of column_2 with a string variable
df1.loc[2, 'column_2'] = 'some string'

# Find the mean of column_2
try:
    mean_column_2 = df1['column_2'].mean()
    print("Mean of 'column_2':", mean_column_2)
except TypeError as e:
    print(f"TypeError: {e}\nCould not calculate the mean of 'column_2' because it contains non-numeric values.")


# # question 06
What do you understand about the windows function in pandas and list the types of windows
functions?In pandas, a window function is a way to perform calculations on a specified window of data. The window is defined by the range of rows that the function operates on, and it can be fixed or sliding. Window functions are useful for performing rolling calculations or calculations that take a certain number of rows into account.

Pandas offers a wide range of window functions that can be used with the rolling() method. Some of the most commonly used window functions are:

sum(): Calculates the sum of the specified window
mean(): Calculates the mean of the specified window
std(): Calculates the standard deviation of the specified window
min(): Calculates the minimum value of the specified window
max(): Calculates the maximum value of the specified window
count(): Counts the number of non-NA/null values in the specified window
apply(): Applies a custom function to the specified window
These window functions can be used with different parameters, such as the window size and the window type (rolling or expanding). The rolling() method takes these parameters as arguments, and it returns a new DataFrame or Series with the calculated values for each window.

Overall, window functions in pandas provide a powerful tool for performing complex calculations on time-series or other types of data that involve sliding or fixed windows.
# # question 07|
Write a code to print only the current month and year at the time of answering this question.
[Hint: Use pandas.datetime function]
# In[15]:


import pandas as pd

current_datetime = pd.datetime.now()
current_month = current_datetime.month
current_year = current_datetime.year

print(f"Current month and year: {current_month}-{current_year}")


# # question 08
Write a Python program that takes in two dates as input (in the format YYYY-MM-DD) and
calculates the difference between them in days, hours, and minutes using Pandas time delta. The
program should prompt the user to enter the dates and display the result.
Here's a Python program that takes in two dates as input and calculates the difference between them in days, hours, and minutes using Pandas timedelta:
# In[ ]:


import pandas as pd

# Prompt the user to enter the two dates
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

# Convert the dates to pandas datetime objects
date1 = pd.to_datetime(date1)
date2 = pd.to_datetime(date2)

# Calculate the timedelta between the two dates
delta = date2 - date1

# Extract the number of days, hours, and minutes from the timedelta
days = delta.days
hours = delta.seconds // 3600
minutes = (delta.seconds % 3600) // 60

# Display the result to the user
print(f"The difference between {date1.date()} and {date2.date()} is {days} days, {hours} hours, and {minutes} minutes.")


# # question 09
Write a Python program that reads a CSV file containing categorical data and converts a specified
column to a categorical data type. The program should prompt the user to enter the file path, column
name, and category order, and then display the sorted data.
# In[ ]:


import pandas as pd

# Prompt the user to enter the file path, column name, and category order
file_path = input("Enter the file path: ")
column_name = input("Enter the column name: ")
category_order = input("Enter the category order (comma-separated values): ").split(",")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Convert the specified column to a categorical data type with the specified category order
df[column_name] = pd.Categorical(df[column_name], categories=category_order)

# Sort the DataFrame by the specified column
df = df.sort_values(by=column_name)

# Display the sorted data to the user
print(df)


# # question 10
# Write a Python program that reads a CSV file containing sales data for different products and
visualizes the data using a stacked bar chart to show the sales of each product category over time. The
program should prompt the user to enter the file path and display the chart.
# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Prompt the user to enter the file path
file_path = input("Enter the file path of the CSV file containing the sales data: ")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Group the data by product category and year, and calculate the sum of sales
grouped_data = df.groupby(['Product Category', 'Year'])['Sales'].sum().unstack()

# Plot a stacked bar chart of the sales of each product category over time
grouped_data.plot(kind='bar', stacked=True)

# Set the chart title and axis labels
plt.title('Sales by Product Category')
plt.xlabel('Year')
plt.ylabel('Sales')

# Display the chart
plt.show()


# # question 11
You are given a CSV file containing student data that includes the student ID and their test score. Write
a Python program that reads the CSV file, calculates the mean, median, and mode of the test scores, and
displays the results in a table.
The program should do the followingM
I Prompt the user to enter the file path of the CSV file containing the student dataR
I Read the CSV file into a Pandas DataFrameR
I Calculate the mean, median, and mode of the test scores using Pandas toolsR
I Display the mean, median, and mode in a table.
Assume the CSV file contains the following columnsM
I Student ID: The ID of the studentR
I Test Score: The score of the student's test.
Example usage of the program:
Enter the file path of the CSV file containing the student data: student_data.csv
+-----------+--------+
| Statistic | Value |
+-----------+--------+
| Mean | 79.6 |
| Median | 82 |
| Mode | 85, 90 |
+-----------+--------+
Assume that the CSV file student_data.csv contains the following data:
Student ID,Test Score
1,85
2,90
3,80
4,75
5,85
6,82
7,78
8,85
9,90
10,85
# In[ ]:


import pandas as pd

# Prompt the user to enter the file path
file_path = input("Enter the file path of the CSV file containing the student data: ")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Calculate the mean, median, and mode of the test scores
mean = df['Test Score'].mean()
median = df['Test Score'].median()
mode = df['Test Score'].mode()

# Display the mean, median, and mode in a table
table = pd.DataFrame({
    'Statistic': ['Mean', 'Median', 'Mode'],
    'Value': [mean, median, mode]
})
print(table)


# In[ ]:




