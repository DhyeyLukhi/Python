import numpy as np
import pandas as pd

dict1 = {
    "Name": ['Dhyey', 'Netra', 'Harry', 'Wish'],
    "Marks": [95, 55, 85, 90],
    "City": ['Mumbai', 'Surat', 'Rampur', 'Anywhere']
}


df = pd.DataFrame(dict1)  # This is just like Excel Sheets, it converts  it into Excel sheets, for faster index and many more
# Here index = row and collunm = collumn
print(df)  # This shows the dictionary as an Excel Sheet
df.to_csv('checking.csv')  # This line creates a checking.csv file to the path
df.to_csv('checking2.csv', index=False)  # This line creates a checking2.csv file to the path
# But you type index=False means this will remove the first column which is known as index and this stores the numbers of rows(number of index)
print(df.head(2))  # If you have too many rows than this will show you the first two rows and other will skip
print(df.tail(2))  # If you have too many rows than this will show you the last two rows and other will skip
print(df.describe())  # This shows you the statistical analysis of the numbers


# dhyey2 = pd.read_csv()   # you can read the .csv file using this line (Put name of the file at pd.read_csv(filename))
# print(dhyey2)
# print(df['Name'][0])  # You can get the value which is at "Name" column and 0th index
# df['Name'][0] = "Vijay"  # And you can change that value by using this line
# This Acutally shows an ERROR, but no worry this works 100%
# print(df['Name'][0])


# df.to_csv('dhyey2.csv')  # Now this changes you do, saves and create a new dhyey2.csv and paste it there
df.index = ['First', "Second", "Third", "Fourth"]  # This will change the value of the index from 1, 2... to First, Second...
print(df)


series = pd.Series(np.random.rand(34))
print(series)  # It gives you a series(series is data structure of Pandas)
print(type(series))  # You can check the type of the seires, and it shows you the "pandas.core.series.Series"
# When you give your datas to pandas, then pandas make index for better work, progress, searching


new = pd.DataFrame(np.random.rand(334, 10), index=np.arange(334))  # np.arange is a function in numpy, just-like range in Python
# It makes a new DataFrame which has 334 rows and 5 columns
print(new)  # If you try to print them, then it shows some of them rows and columns of strating and ending, but at the end it shows you that how many columns and rows it has
type(new)  # if you try to print the type of new, it shows the "pandas.core.frame.DataFrame"
print(new.describe())
print(new.dtypes)  # It shows that which type of data types are used in the DataFrame


# new[0][0] = "Dhyey"  # You can still change the value of the particular item
print(new)
print(new.dtypes)  # Generally a column has only one DataType in Pandas, But when you change value from one of them, Datatype covnerts to Objct from anything
print(new.index)  # You can print the index of the file
print(new.columns)  # You can also print the columns of the file


print(new.to_numpy())  # You can create the numpy array of that file

new.sort_index(axis=0, ascending=True)  # This will sort the index to ascending order
# change the ascending to False and this will sort the DataFrame to descending order
print(new)


print(type(new[0]))  # You can check the type of the index
#
# new.loc[0][0] = "DHYEY"
print(new)
print(new.head())
#
# new3 = new  # This will not work in DataFrame, this works like a pointer in DataFrame which makes a pointer "new3" which points the "new" DataFrame
# new2 = new[:]  # You can copy the DataFrame to another DataFrame using this
new2 = new.copy()  # The copy function can also make the copy of the function
print(new)
print(new2)
#
#
new.columns = list("ABCDEFGHIJ")  # This will rename the columns of the DataFrame - A, B, C, D...I, J.
print(new)
#
#
new.loc[0, 0] = "Dhyey2"  # As you know that you can't change the value of the DataFrame
# But you can use the .loc function to change the value wihtout any ERROR
print(new)
#
new = new.drop(0, axis=1)  # Now sometimes you have to remove the column then you can use the drop function to remove the column
# Here axis=1 which indicates the column and 0 is the name of label
# new.drop([1, 5] axis=0, inplace=True)  # This will remove the index no. 1 and 5 from the DataFrame
# Here inplace=True, because this will apply the function temporary, it does not saev that
# so inplace=True will save the change to the original DataFrame
new.drop(['A', 'C'], axis=1)  # So this will remove the 'A' and 'C' column in the DataFrame
print(new)
#
#
print(new.loc[[1, 2], ['C', 'D']])  # This will print the value of index no. 1, 2 at column no. 'C', 'D'
print(new.loc[(new['A'] < 0.5)])  # This will print all the values of column no. 'A' which is lower than 0.5
#
#
print(new.loc[(new['A'] < 0.5) & (new['D'] > 0.5)])  # This will print all the value of column 'A' which is lower than 0.5 and column 'D' which is higher than 0.5
print(new['B'].isnull())  # This will show that in the column 'B' where is the value of index is Null
# There is also a notnull() function which tells you that where the values are not Null (just like oppostie function of isnull())

# new.loc[:, ['B']] = 95  # This will set all the value of index which is at column 'B' to 95
new.reset_index(drop=True, inplace=True)  # This will reset the indext from 1 to ...
# Here drop=True, because when you use this function it will add another column 'index' so this will remove that index
# inplace=True, because this will only do this one time, inplace function is used to save the change to the original DataFrame

print(new.iloc[[0, 5], [1, 2]])  # This will print the values which are at column no. [0, 5] (counting- 0='A', 1='B', 2='C'...) and at index no. 1, 2
print(new.iloc[0, 2])  # this will print the value which is at index no. 0 and column no. 2


"""Make a new DataFrame for below commands"""


new.dropna()  # This will remove all the index which has "None" value
new.dropna(how='all', axis=1)  # This will not remove the column until all the value of that column is not gone None
new.drop_duplicates(subset=['A'])  # This will remove the duplicate of the column 'A'
new.drop_duplicates(subset=['A'], keep='first')  # keep='first', this will keep the first value and remove it's repeated value from the column
# keep='last' will keep the last value of the repeated and remove other value from the column
# keep=False will remove all the repeated values including original

print(new.info())  # This will print the information of the DataFrame
print(new['A'].value_counts(dropna=False))  # This will print that values of column 'A' is coming how much times in the DataFrame
# put dropna=True and it will not count the NaN values


"""
 FOR MORE INFORMATION VISIT WEBSITE = https://pandas.pydata.org/docs/reference/io.html 
"""
