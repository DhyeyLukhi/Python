import numpy as np
import pandas as pd

"""
First of all:
--> The Pandas is an open source data analysis library witten in Python
--> If you used Excel sheets then you might miss some extraordinary abilities of Python
--> It use the power and speed of numpy(numpy library written in C language), which make data analysis and preprocessing easy for data scientist
--> It provides rich and higly robust data opoerations


On Other Hand:
--> The Jupyter Notebook is an open-source web application that alows yout to creat and share documents that contain live code, equations, visualizations and narrative text
--> The Notebook has support for over 40 programming languages, including Pythn, R, Julia and Scala.
--> Notebooks can be shared with others using email, Dropbox, GitHub and the Jupyter Notebook Viewer.
--> You code can produce rich, interactive output

"""


"""
Use only name in Jupyter notebook to print the value of that DataType
there is no print statement in Jupyter notebook which is online
"""


dict1 = {
    "Name": ['Dhyey', 'Netra', 'Harry', 'Wish'],
    "Marks": [95, 55, 85, 90],
    "City": ['Mumbai', 'Surat', 'Rampur', 'Anywhere']
}

df = pd.DataFrame(dict1)  # This is just like Excel Sheets, it converts  it into Excel sheets, for faster index and many more
# Here index = row and collunm = collumn
# print(df)  # This shows the dictionary as an Excel Sheet
df.to_csv('checking.csv')  # This line creates a checking.csv file to the path
df.to_csv('checking2.csv', index=False)  # This line creates a checking2.csv file to the path
# But you type index=False means this will remove the first column which is known as index and this stores the numbers of rows(number of index)
# print(df.head(2))  # If you have too many rows than this will show you the first two rows and other will skip
# print(df.tail(2))  # If you have too many rows than this will show you the last two rows and other will skip
# print(df.describe())  # This shows you the statistical analysis of the numbers


#
# dhyey2 = pd.read_csv()   # you can read the .csv file using this line (Put name of the file at pd.read_csv(filename))
# print(dhyey2)
# print(df['Name'][0])  # You can get the value which is at "Name" column and 0th index
# df['Name'][0] = "Vijay"  # And you can change that value by using this line
# This Acutally shows an ERROR, but no worry this works 100%
# print(df['Name'][0])


# df.to_csv('dhyey2.csv')  # Now this changes you do, saves and create a new dhyey2.csv and paste it there
# df.index = ['First', "Second", "Third", "Fourth"]  # This will change the value of the index from 1, 2... to First, Second...
# print(df)

"""
*********************************************************************************************************************************
******************** Above mentioned are most common steps and codes in the Pandas and Jupyter **********************************
*********************************************************************************************************************************
"""

series = pd.Series(np.random.rand(34))
# print(series)  # It gives you a series(series is data structure of Pandas)
# print(type(series))  # You can check the type of the seires, and it shows you the "pandas.core.series.Series"
# When you give your datas to pandas, then pandas make index for better work, progress, searching


new = pd.DataFrame(np.random.rand(334, 10), index=np.arange(334))  # np.arange is a function in numpy, just-like range in Python
# It makes a new DataFrame which has 334 rows and 5 columns
# print(new)  # If you try to print them, then it shows some of them rows and columns of strating and ending, but at the end it shows you that how many columns and rows it has
# print(type(new))  # if you try to print the type of new, it shows the "pandas.core.frame.DataFrame"
# print(new.describe())
# print(new.dtypes)  # It shows that which type of data types are used in the DataFrame


# new[0][0] = "Dhyey"  # You can still change the value of the particular item
# print(new)
# print(new.dtypes)  # Generally a column has only one DataType in Pandas, But when you change value from one of them, Datatype covnerts to Objct from anything
# print(new.index)  # You can print the index of the file
# print(new.columns)  # You can also print the columns of the file


new.to_numpy()  # You can create the numpy array of that file
# print(new.to_numpy())  # Now, it's Datatype stays Object, because there is one string between the float so...


# print(new.T)  # It transposes the file (transfer the no. rows into no. of columns and transfer the no. columns into no. of rows)
print(new)
new.sort_index(axis=0, ascending=False)  # You can sort the DataFrame using this fucntion
# Here axis=0 means the index (axis=1 means the columns) and ascending=false means this will sort the DataFrame in the Descening order, Default value of the ascending is "True"

# new[0][0] = 0.53226598
print(new[0])  # This will print the first column of the DataFrame
print(type(new[0]))  # We can see that type of the first column of the DataFrame is "pandas.core.series.Series"


# new2 = new  # Some of the Programming logics does not work as we think
# In General above line means that there comes a new variable (new2) with the value of another variable (new)
# But, in Jupyter notebook this line works as a pointer, whereever you change the value of new2, evertime the value in new also got change, becasue this is a pointer not another variable
# print(new2)  # If we print the "new2" then you got the result what you thoght.
# new2[0][0] = "Dhyey"  # But if you tried th change the value of "new2" and then try to print the "new"...
# print(new)  # Then you might get shocked
# print(new2)

new3 = new.copy()  # This will make another DataFrame new3 which is a copy of "new" DataFrame
new4 = new[:]  # This will make another DataFrame new4 which is a copy of "new" DataFrame

# new.loc[0][0] = "Dhyey"  # You can use the .loc function to change the value, and it will not show any ERROR
# print(new)

new.columns = list('ABCDEFGHIJ')  # This way you can rename your column as A B C D E F G H J
# print(new)
# new.loc[0, 0] = "Dhyey2"  # And now if you try to change the value then you have to use the name of new column because it is changes above
# Here the new name of column A B C... so it will make a new column with the title 0 and there it insert the value "Dhyey2"
# print(new)
# And it looks guly because there are too many NaN values
# print(new.drop(['A', 'C'], axis=1))  # This way you can drop one or more columns
# print(new.drop([1, 3], axis=0))  # This way you can drop one or more indexes
# new = new.drop(0, axis=1)  # only using new.drop() function can only drop the column for one time, after this line the DataFrame remains unchanged
# But, by going this way your change will be saved in itself if you don't put "new = " then output might unexpected
# print(new.drop([1, 3], axis=0, inplace=True))  # And there is another function called inplace in some of the DataFrames which modified the orignial DataFrame
# print(new)


# print(new.loc[[1, 2], ['C', 'D']])  # This will print only index no. 1 and 2 and column 'C' and 'D'
# print(new.loc[:, ['C', 'D']])  # Now you will get every index for the column no. 'C' and 'D'
# print(new.loc[[1, 2], :])  # Now you will get every column for the index no. 1 and 2
# In the Above statements ":" was taken as the whole number of indexes/columns, so using ":", you can get the output for every index/column
# print(new.loc[:, :])  # And this is just like printing "new"


# print(new.loc[(new['A'] < 0.5)])  # This shows that in the 'A' Column which index has the value less than 0.5
# print(new.loc[(new['A'] < 0.5) & (new['D'] > 0.5)])  # And you can go more complex like this

print(new.head(5))
print(new.iloc[0, 5])  # This just simply print the value which is on index no.0 and column no.5 (value:column no. - 0=A, 1=B, 2=C, 3=D, 4=E,...)

print(new.iloc[[0, 5], [4, 9]])  # This simply print the value which is one index no. 0, 3 and column no. 4, 9 (here it is 'E' and 'J')


# Now sometimes some of the reasons, your index of the DataFrame goes complex, and that time you need to reset it
new.reset_index(drop=True, inplace=True)  # This way you can reset your DataFrames index
# But this function, also add another index bydefault, so you can drop it using drop function as mentioned in the line
# And you can save you change using inplace function
print(new)


print(new['B'].isnull())  # It shows you that in the "B" column which index's value is 0, and where it shows "True" there is the 0
# Above line may not porperly work in PyCharm but, work perfectly in Jypyter Notebook local host website


new.loc[:, ['B']] = None  # Now you can see that all the value in the "B" column changes to "None"
print(new)

new.dropna(inplace=True)  # This will remove all the line which has NaN
# But above code will remove the index/column if there is a single missing element in the DataFrame
new.dropna(how='all', axis=1)  # But if you set "how=True" then it will not remove the index/column until all the elements are not gone missing
new.drop_duplicates(subset=['A'], keep='first')  # Now this will remove the dupicaltes from the "A" column
# Here keep='first' means it saves the first value and if it repeats, then it will remove the repeated values
# If we put keep='last' then it saves the last values of the duplicates and remove from first to second-last duplicates
# If we put keep='False' then it will remove every duplicate incluing original, means every repeated item will be deleted including the original
