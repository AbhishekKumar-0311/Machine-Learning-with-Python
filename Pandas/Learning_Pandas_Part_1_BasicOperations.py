# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ### Prepared by Abhishek Kumar
# ### https://www.linkedin.com/in/abhishekkumar-0311/
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# +
# To get multiple outputs in the same cell

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# %matplotlib inline
# -

# # A.) Data Input/Output
# ## 1. Dataframe creation

# ### There are multiple ways to create a dataframe. 
# 1. Through lists, which i have demonstrated here.
# 2. Through dictionaries
# 3. Using pd.DataFrame()
# 4. Using pd.from_records()

# +
salary = [['Google', 'Machine Learning Engineer', 121000],
['Google', 'Data Scientist', 109000],
['Google', 'Tech Lead', 129000],
['Facebook', 'Data Scientist', 103000]]

columns_name=['Company', 'Job','Salary']

emp_df = pd.DataFrame(salary,columns=columns_name)
emp_df
# -

# ## 2. Import - Creating a dataframe from external file, here csv

# +
# cov_df = pd.read_csv('E:\VCS\GitHub\Machine-Learning-with-Python\data\Data USA Cart\covid19.csv')
# cov_df.head()
# -

# ## 3. Export - Writing a dataframe to external file, here csv

# +
#pd.to_csv('path\df.csv')
# -

# # B.) Data Operations

# ## 1. Copying - Creating a new dF from existing dF
# ### SAS
# 1. In existing dataFrame - data xyz; set xyz; run;
# 2. In new dataFrame - data abc; set xyz; run;
#
# ### Python
# 1. In existing dataFrame - df_have = df.have
# 2. In new dataFrame - df_want = df.have.copy()
#
# Note : The manipulations in python can be chained on the right hand side.
# 1. Copying through variables - Changes made in new dataframe are also reflected in the old dataframe since the new variable 'emp_df_0' is just a pointer to old one 'emp_df'.
# 2. .copy() - df.copy() creates an independent copy of the dataset

# +
# Copying through variables

emp_df_0 = emp_df
emp_df_0

# +
# Updating the new dF
emp_df_0['Salary']=emp_df_0['Salary']+1000

# Comparison of dataframes
emp_df_0 == emp_df

# Both the dF have the same values
emp_df_0
emp_df

# +
# Using Copy() to create a new dF 
emp_df_1 = emp_df.copy() # df.copy(deep=false) - does not create an independent copy

# Updating the new dF
emp_df_1['Salary']=emp_df_1['Salary']+1000

# Comparison of dataframes
emp_df_1 == emp_df

# Both the dF have the same values
emp_df_1
emp_df
# -

# ###  Analysis of dataFrame Comparison 

# +
# Comparison of dataframes  with == : It does not handle missing ( NaN ) values
# Return False if there are NaN values.
cmp_1 = emp_df_1 == emp_df
cmp_1

# Comparison Analysis
cmp_1.all()
cmp_1.all().sum()

# Comparing 2 dataframes with .eq() : It does not handle missing ( NaN ) values
# Return False if there are NaN values.
emp_df.eq(emp_df_0).all()
emp_df.eq(emp_df_1).all().sum()

# Comparing 2 dataframes with .equals() : It handles missing ( NaN ) values
emp_df.equals(emp_df_0)
emp_df.equals(emp_df_1)
# -

# ## 2. Creation of new columns - Not based on condition
# ### SAS
# 1. In existing dataFrame - data xyz; set xyz; new_col = 'i m new'; run;
# 2. In new dataFrame - data abc; set xyz;  new_col = 'i m new'; run;
#
# ### Python
# 1. In existing dataFrame - df_have['new_col'] = 'i m new'
# 2. In new dataFrame - df_want = df.have.copy() ; df_want['new_col'] = 'i m new'
#
# Note : The manipulations in python can be chained on the right hand side.

# +
# Column created in Existing dataFrame

emp_df_1['Hike_amt'] = emp_df_1['Salary']*0.1
emp_df_1

# +
# Creating a new dataFrame, here using copy()
emp_df_2 = emp_df_1.copy()

# Column created in new dataFrame
# Hike_amt is same for all employess - 15%

emp_df_2['Hike_amt'] = emp_df_1['Salary']*0.15
emp_df_2
emp_df_1


emp_df_2['WFH_Status'] = 1
emp_df_2['Gender'] = 'M'
emp_df_2
# -

# ## 3. Creation of new columns - Based on If-then/else condition

# ### .assign() and .apply()

# +
emp_df_3 = emp_df_2.copy()

# Bonus_amt is decided based on Job Role
# DS - 20% of Salary
# MLE - 15% of Salary
# TL - 10% of Salary

def bonus(row):
    if row['Job'] == 'Data Scientist':
        return row['Salary']*0.2
    elif row['Job'] == 'Machine Learning Engineer':
        return row['Salary']*0.15
    elif row['Job'] == 'Tech Lead':
        return row['Salary']*0.1

emp_df_3a =  emp_df_3.assign(bonus_amt=emp_df_3.apply(bonus,axis=1))
emp_df_3a =  emp_df_3a.assign(Bonus_amt=emp_df_3a.apply(bonus,axis=1))

emp_df_3a


# -

# ### .apply - to apply user-defined function

# +
# Bonus_amt is decided based on Job Role
# DS - 20% of Salary
# MLE - 15% of Salary
# TL - 10% of Salary

def bonus(row):
    if row['Job'] == 'Data Scientist':
        return row['Salary']*0.2
    elif row['Job'] == 'Machine Learning Engineer':
        return row['Salary']*0.15
    elif row['Job'] == 'Tech Lead':
        return row['Salary']*0.1
    
# Creation of dataframe
_emp_df_3a = emp_df_2.copy()

_emp_df_3a['Bonus_amt'] = _emp_df_3a.apply(bonus,axis=1)
_emp_df_3a
# -

# ### .loc()

# +
emp_df_3b = emp_df_2.copy()
emp_df_3b
# Creating a new column Bonus_amt based on Job
# DS - 20% of Salary
# MLE - 15% of Salary
# TL - 10% of Salary

emp_df_3b.loc[emp_df_3b['Job'] == 'Data Scientist', 'Bonus_amt' ] = emp_df_3b['Salary']*0.2
emp_df_3b
emp_df_3b.loc[emp_df_3b['Job'] == 'Machine Learning Engineer', 'Bonus_amt' ] = emp_df_3b['Salary']*0.15
emp_df_3b
emp_df_3b.loc[emp_df_3b['Job'] == 'Tech Lead', 'Bonus_amt' ] = emp_df_3b['Salary']*0.1
emp_df_3b
# -

# ### .loc()

# +
# Updating the column Bonus_amt on which the condition is based

emp_df_3b.loc[emp_df_3b.Bonus_amt >= 20000, 'Bonus_amt'] = emp_df_3b.Bonus_amt-2000
emp_df_3b
# -

# ### .apply() and lambda Fx

# +
# Using lambda function to 

emp_df_3b2 = emp_df_3b.copy()
emp_df_3b2['Bonus_amt'] = emp_df_3b['Bonus_amt'].apply(lambda x: x+100 if x >= 20000 else x)
emp_df_3b2

# -

# ### np.where()

emp_df_3b['Bonus_amt'] = np.where(emp_df_3b['Bonus_amt'] >= 20000, emp_df_3b.Bonus_amt+2000, emp_df_3b.Bonus_amt)
emp_df_3b

# ### List comprehension -  another way to create another column conditionally.
# 1. When working with object dtypes in columns, list comprehensions typically outperform most other methods.

emp_df_3b['Bonus_amt'] = [ x+1000 if x <= 20000 else x for x in emp_df_3b['Bonus_amt'] ]
emp_df_3b

# ### np.select() - If there are more than two conditions then use np.select

# +
emp_df_3c = emp_df_2.copy()
emp_df_3c

# Creating a new column Bonus_amt based on Job
# DS - 20% of Salary
# MLE - 15% of Salary
# TL - 10% of Salary

conditions = [
    (emp_df_3c['Job'] == 'Data Scientist'),
    (emp_df_3c['Job'] == 'Machine Learning Engineer'),
    (emp_df_3c['Job'] == 'Tech Lead')]

choices = [emp_df_3c.Salary*.20, emp_df_3c.Salary*.15, emp_df_3c.Salary*.10]

emp_df_3c['Bonus_amt'] = np.select(conditions, choices, default=10000)

emp_df_3c
# -

# ### Use If-else condition to REPLACE MISSING VALUES with CUSTOM VALUES

# +
# Setup : for dataframe creation
emp_df_3d = emp_df_3c.copy()

# Setup : Updating few values with NaN

emp_df_3d['Bonus_amt'] = np.where(emp_df_3d['Bonus_amt'] <= 21000, np.NaN, emp_df_3d['Bonus_amt'] )
emp_df_3d

# Updating the missing values (NaN) with any custom value, here 10000

emp_df_3d.loc[emp_df_3d['Bonus_amt'].isna(), 'Bonus_amt' ] = 10000
emp_df_3d

# +
#Mean Imputation
#Description
#Impute the mean value at all the missing values of the column 'Product_Base_Margin' and then print the percentage of missing values in each column.

import numpy as np
import pandas as pd
df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
df.loc[np.isnan(df['Product_Base_Margin']), ['Product_Base_Margin']] = df['Product_Base_Margin'].mean()
print(round((100*(df.isnull().sum()/len(df.index))),2))#Round off to 2 decimal places.

# -

# ## 4. Filtering out Rows from dataframe
#
# 1. Equivalent of IF Statement and WHERE statement/option in SAS.
# 2. Here, Rows are filtered out to either update the existing dataframe or create a new dataframe
#
# #### i.   Positional indexing : df.iloc[np.where(filter_condition)]  - fast
# #### v.  Label indexing         : df.loc[df['A'].isin(['foo'])] - fast
# #### v.  Label indexing         : df.loc[filter_condition] - slow 
# #### iv. Boolean indexing    : df[filter_condition] - slower ()
# #### vi.  df.query() API         : df.query('(col_nm <operator> value)') - slowest (for large data, the query is very efficient. More so than the standard approach)
#     
# filter_condition, something like df.A=='foo' 

# ### Boolean Indexing

# +
# Setup for dataframe creation

emp_df_4a = emp_df_3c.copy()
emp_df_4a

emp_df_4b = emp_df_3c.copy()

# Setup : Updating few 'Bonus_amt' values with NaN

emp_df_4a['Bonus_amt'] = np.where(emp_df_4a['Bonus_amt'] <= 21000, np.NaN, emp_df_4a['Bonus_amt'] )
emp_df_4a

# Filtering out rows in the existing dataframe
# Here, only the rows with the non-missing Bonus_amt are retained - .notna()
emp_df_4a = emp_df_4a[emp_df_4a.Bonus_amt.notna()]
emp_df_4a

# Filtering out rows to create a new dataframe
emp_df_4b_ = emp_df_4b[(emp_df_4b.Bonus_amt > 13100) & (emp_df_4b.Hike_amt > 16000) ]
emp_df_4b_
# -

# Note:
# 1. The mask (boolean indexes) can be created in different ways.
#     
#     a. Creating a series of boolean indexes : mask = df['A'] == 'foo'
#     
#     b. Using the underlying numpy array and forgo the overhead of creating another pd.Series : mask = df['A'].values == 'foo'
#     
#     c. Instead of df[mask] we will do this : pd.DataFrame(df.values[mask], df.index[mask], df.columns).astype(df.dtypes)
#     
#     d. Using pd.Series.isin to account for each element of df['A'] being in a set of values

# ### .iloc[ ] and np.where()  - Fast

# +
# Setup for dataframe creation

emp_df_4c = emp_df_3c.copy()
emp_df_4c

emp_df_4c_1 = emp_df_4c.iloc[np.where(emp_df_4c['Bonus_amt'] >= 20000)]
emp_df_4c_1
# -

# ### .loc[ ] or without .loc[ ] with .isin() - fast

# +
# Setup for dataframe creation

emp_df_4d = emp_df_3c.copy()
emp_df_4d


# Comapring with a list of values , use .isin() 
emp_df_4d0 = emp_df_4d.loc[emp_df_4d.Job.isin(['Tech Lead', 'Data Scientist'])]
emp_df_4d0


# Showing 'not in' feature through ~ and .isin()  
emp_df_4d1 = emp_df_4d[~emp_df_4d.Job.isin(['Tech Lead', 'Data Scientist'])]
emp_df_4d1
# -

# ## 5. Selecting and Dropping columns

# 1. Equivalent of KEEP and DROP statement/option in SAS

# #### There are 3 popular techniques of COLUMNS SELECTION, either for displaying or else for creaing a new DataFrame
# #### i. df_name[['col_a','col_b','col_c']] - Variants can be : df_name[columns_list]
# #### ii. Positional indexing - df_name.iloc[ : , m:n]
# #### iii. Label Indexing - df_name.loc[ : , 'col_m':'col_n'] - Variants are : df_name.loc[ : , ['col_a','col_b','col_c']] : df_name.loc[ : , columns_list]
# #### iv. pd.DataFrame( df , columns = columns_list 
#
# #### There are 2 popular techniques of DROPPING COLUMNS
# #### v. df.drop('col_a') or df.drop(['col_a','col_b','col_c']) or df.drop(columns_list)
# #### vi. df.pop('col_a')

# ### i. df_name[columns_list]

# +
# Setup : DataFrame creation
emp_df_5a = emp_df_3a.copy()

emp_df_5b = emp_df_3a.copy()


# Checking no. of columns in emp_df_5a
emp_df_5a.shape[1]

# Displaying the dataframe emp_df_5a with selected columns
emp_df_5a[['Company','Job','Salary']]

# Checking the no. of columns again - Now it is still the same as actual, since the previous step was only for displaying df
emp_df_5a.shape[1]
emp_df_5a

# Selecting few columns and Re-assigning to the original dataframe emp_df_5a
emp_df_5a = emp_df_5a[['Company','Job','Salary']]

# Checking the no. of columns again - Now it is reduced to 3
emp_df_5a.shape[1]
emp_df_5a


# Creating a list of column names and then passing the list as parameter
colums_list = ['Company','Job','Salary','Gender']

# Selecting few columns and Re-assigning to the original dataframe emp_df_5a
emp_df_5b = emp_df_5b[colums_list]
emp_df_5b
# -

# ### ii. Positional indexing - df_name.iloc[ : , m:n]

# +
# Setup : DataFrame creation
emp_df_5c = emp_df_3a.copy()
emp_df_5c
emp_df_5d = emp_df_3a.copy()

# Here m and n are the columns indexes. while 'n' is exclusive.
# So, it keeps column 1 and 2
emp_df_5c = emp_df_5c.iloc[ : , 1:3]
emp_df_5c


emp_df_5d
# Here m and n are the columns indexes. while 'n' is EXCLUSIVE.
# So, it keeps column 1 and 2
emp_df_5d_new = emp_df_5d.iloc[ : , 1:3]
emp_df_5d_new


# emp_df_5d_new['test_col'] = 'test_value'
# emp_df_5d_new
# emp_df_5d

# emp_df_5d_new['Salary'] = 1000
# emp_df_5d_new
# emp_df_5d

# -

# ### iii. Label Indexing - df_name.loc[ : , 'col_m':'col_n'] - Variants are : df_name.loc[ : , ['col_a','col_b','col_c']] : df_name.loc[ : , columns_list]

# +
# Setup : DataFrame creation
emp_df_5e = emp_df_3a.copy()
emp_df_5e
emp_df_5f = emp_df_3a.copy()

# Here col_m and col_n are the column names/Labels. while 'col_n' is INCLUSIVE.
# So, it keeps column 1 and 2
emp_df_5e = emp_df_5e.loc[ : , 'Company':'Hike_amt']
emp_df_5e
# -

# ### iv. pd.DataFrame( df , columns = columns_list )

# +
# Setup : DataFrame creation
emp_df_5f = emp_df_3a.copy()
emp_df_5f

columns_list = ['Company', 'Job', 'Salary', 'Hike_amt']

# Creating a new dF with the columns list
emp_df_5f_0 = pd.DataFrame(emp_df_5f, columns= columns_list)
emp_df_5f_0

# Updating the existing dF with the columns list
emp_df_5f = pd.DataFrame(emp_df_5f, columns= columns_list)
emp_df_5f
# -

# ### v. df.drop('col_a') or df.drop(['col_a','col_b','col_c']) or df.drop(columns_list)

# #### DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')[source]
#
# 0. Return new object with labels in requested axis removed.
# 1. labels : single label or list-like - Index or column labels to drop.
# 2. axis : int or axis name - Whether to drop labels from the index (0 / ‘index’) or columns (1 / ‘columns’).
# 3. index, columns : single label or list-like
# 4. Alternative to specifying axis (labels, axis=1 is equivalent to columns=labels).
# 5. level : int or level name, default None
# 6. inplace : bool, default False - If True, do operation inplace and return None.
# 7. errors : {‘ignore’, ‘raise’}, default ‘raise’ - If ‘ignore’, suppress error and existing labels are dropped.

# +
# Setup : DataFrame creation
emp_df_5g = emp_df_3a.copy()
emp_df_5g
emp_df_5h = emp_df_3a.copy()

# Reflecting the column drop in the existing dataframe
emp_df_5g = emp_df_5g.drop('bonus_amt', axis=1)
emp_df_5g
# The above result could also be achieved using 'inplace=True' option
# Also, error = ignore, to ignore errors in case of missing columns
columns_list = ['Company', 'Job', 'Salary', 'Hike_amt']

emp_df_5h.drop(columns_list, axis=1, inplace = True, errors = 'ignore')
emp_df_5h
# -

# Note:
#
# 1. It is important to realize that there could be various ways to get the 'columns_list' that is passed in df.drop().
# 2. df.loc[ ]
# 3. df.iloc[ ]
# 4. df.columns[ ]

# ### vi. df.pop('col_a')

# #### DataFrame.pop(self: ~FrameOrSeries, item) → ~FrameOrSeries[source]
#
# 0. Return item and drop from frame. Raise KeyError if not found.
#
# 1. Parameters - item : str - Label of column to be popped.
# 2. Returns - Series

# +
# Setup : DataFrame creation
emp_df_5i = emp_df_3a.copy()
emp_df_5i
emp_df_5j = emp_df_3a.copy()


# Only a single column can be popped out.
emp_df_5i.pop('bonus_amt')
emp_df_5i
emp_df_5j
# the popped series can be stored in a new variable and can be re-used
pop_var = emp_df_5j.pop('bonus_amt')

# new_df['new_col'] = pop_var # this will throw error, as the dataframe does not already exist
# new_df

# Instead use pd.dataFrame, to create a new dataframe 
new_df = pd.DataFrame(pop_var)
new_df

new_df['col2'] = new_df
new_df
# -

# ## 6. Selection of rows based on their serial number in dataFrame
#
# ### SAS Counterpart
# 1. Sequential  - FIRSTOBS= and OBS=
# 2. Random Access - POINT=
#
# ### Pandas
#
# 1. Sequential  - .head( ) and .tail( ) , also df.iloc[ ] and df.loc[ ]
# 2. Random Access - df.iloc[ ] and df.loc[ ]

# Setup : DataFrame creation
emp_df_6 = emp_df_3a.copy()
emp_df_6

# +
# SEQUENTIAL ACCESS

# By default, it displays 5 rows from top
emp_df_6.head()

# It displays 3 rows from top
emp_df_6.head(3)

# By default, it displays 5 rows from bottom
emp_df_6.tail()

# It displays 3 rows from top
emp_df_6.tail(3)

# Combination of head and tail results in slicing of dF
emp_df_6.head(3).tail(1)

# +
# SEQUENTIAL ACCESS
emp_df_6.iloc[0:2]            # end-index in EXCLUSIVE
emp_df_6.loc[0:2]             # end-index in INCLUSIVE

# RANDOM ACCESS
emp_df_6.iloc[[2,0,3]]        # INVALID indices/labels will throw error - "indices are out-of-bounds"

# Any missing label in .loc[ ] will raise KeyError
emp_df_6.loc[[2,0,3]]
# -

# Note :
# 1. Passing list-likes to .loc or [] with any missing label will raise KeyError in the future, you can use .reindex() as an alternative.

# ## 7. Renaming Column names

# ### i. df.rename( )
# ### ii. df.columns = col_list
# ### iii. df.set_axis( )

# #### i. DataFrame.rename(self, mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore')[source]
# df.rename() - Alter axes labels.
#
# 0. Function / dict values must be unique (1-to-1). Labels not contained in a dict / Series will be left as-is. Extra labels listed don’t throw an error.
#
# 1. Parameters : mapperdict-like or function : Dict-like or functions transformations to apply to that axis’ values. Use either mapper and axis to specify the axis to target with mapper, or index and columns.
# 2. indexdict-like or function : Alternative to specifying axis (mapper, axis=0 is equivalent to index=mapper).
# 3. columnsdict-like or function : Alternative to specifying axis (mapper, axis=1 is equivalent to columns=mapper).
# 4. axisint or str : Axis to target with mapper. Can be either the axis name (‘index’, ‘columns’) or number (0, 1). The default is ‘index’.
# 5. copybool, default True : Also copy underlying data.
# 6. inplacebool, default False : Whether to return a new DataFrame. If True then value of copy is ignored.
# 7. levelint or level name, default None : In case of a MultiIndex, only rename labels in the specified level.
# 8. errors{‘ignore’, ‘raise’}, default ‘ignore’ : If ‘raise’, raise a KeyError when a dict-like mapper, index, or columns contains labels that are not present in the Index being transformed. If ‘ignore’, existing keys will be renamed and extra keys will be ignored.
# 9. Returns DataFrame - DataFrame with the renamed axis labels.
# 10. Raises KeyError - If any of the labels is not found in the selected axis and “errors=’raise’”.

# Setup : DataFrame creation
emp_df_7 = emp_df_3a.copy()
emp_df_7

# #### Using AXIS style parameters

# +
emp_df_7.rename(str.lower , axis='columns')                 # All columns to LOWERCASE
emp_df_7.rename(str.upper , axis='columns')                 # All columns to UPPERCASE
emp_df_7.rename(str.title , axis='columns')                 # All columns to TITLECASE
emp_df_7 

# Include inplace = True to modify the existing dataFrame

# +
# Setup : DataFrame creation
emp_df_7a = emp_df_3a.copy()
emp_df_7a

# Requires a dictionary of old names and new names to be passed to parameter columns=
emp_df_7a.rename(columns={'bonus_amt':'Dup_Bonus_Amt'})
emp_df_7a

# Include inplace = True to modify the existing dataFrame
# -

# #### ii. df.columns = col_list

# +
# Setup : DataFrame creation
emp_df_7c = emp_df_3a.copy()
emp_df_7c

# Assign columns list into df.columns

emp_df_7c.columns = emp_df_7c.columns.str.replace('_',' ')
emp_df_7c
# -

# #### iii. df.set_axis( )

# #### DataFrame.set_axis(self, labels, axis=0, inplace=False)[source]
# Assign desired index to given axis.
# Indexes for column or row labels can be changed by assigning a list-like or Index.
#
# 1. Parameters - labelslist-like, Index : The values for the new index.
# 2. axis{0 or ‘index’, 1 or ‘columns’}, default 0 :The axis to update. The value 0 identifies the rows, and 1 identifies the columns.
# 3. inplacebool, default False : Whether to return a new %(klass)s instance.
#
# 4. Returns - renamed%(klass)s or None : An object of same type as caller if inplace=False, None otherwise.

# +
# Setup : DataFrame creation
emp_df_7d = emp_df_3a.copy()
emp_df_7d

# Full list of labels is passed as a list in set_axis() method
emp_df_7d.set_axis(['1','2','3','4','5','6','7','8'], axis='columns', inplace = True)
emp_df_7d
# -

# ## 8. Sorting + Removing Duplicate rows + Keeping Duplicate rows
# ### SAS
# 1. PROC SORT - To sort on columns and return the existing sorted dataset or new dataset
# 2. PROC SORT (nodupkey/nodup/noduprecs) - Sort and remove duplicate records on sort keys
# 3. PROC SORT (dupout)- Sort and remove and store duplicate records on sort keys in a new dataset
#
# ### Python
# 1. df.sort_values() - sort rows based on key columns. Inplace parameter enables to update same dF or create new dF.
# 2. Sorting as well as removing duplicate rows is a 2-step and independent process unlike Proc sort in SAS. But fortunately, the chaining method makes it look like a one step.
#     df.drop_duplicates() - remove the duplicate rows based on key columns.
# 3. df.duplicated() - return duplicated rows

# #### i. DataFrame.sort_values(self, by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False)[source]
# Sort by the values along either axis.
#
# 1. Parameters - bystr or list of str : Name or list of names to sort by.
#
# if axis is 0 or ‘index’ then by may contain index levels and/or column labels.
# if axis is 1 or ‘columns’ then by may contain column levels and/or index labels.
# Changed in version 0.23.0: Allow specifying index or column level names. - axis{0 or ‘index’, 1 or ‘columns’}, default 0 - Axis to be sorted.
#
# 2. ascending - bool or list of bool, default True : Sort ascending vs. descending. Specify list for multiple sort orders. If this is a list of bools, must match the length of the by.
#
# 3. inplace - bool, default False -: If True, perform operation in-place.
#
# 4. kind - {‘quicksort’, ‘mergesort’, ‘heapsort’}, default ‘quicksort’ - mergesort is the only stable algorithm. For DataFrames, this option is only applied when sorting on a single column or label.
#
# 5. na_position - {‘first’, ‘last’}, default ‘last’ : Puts NaNs at the beginning if first; last puts NaNs at the end.
# 6. ignore_index - bool, default False : If True, the resulting axis will be labeled 0, 1, …, n - 1.
# 7. Returns - sorted_objDataFrame or None : DataFrame with sorted values if inplace=False, None otherwise.

# +
# Setup : DataFrame creation
emp_df_8a = emp_df_3a.copy()
emp_df_8a

# Sort and create a new dF. Existing dF is not sorted.
emp_df_8a1 = emp_df_8a.sort_values(['Job','Salary'], ascending = True, inplace = False )
emp_df_8a1

# Sort and save the existing dF, using INPLACE = TRUE
emp_df_8a.sort_values(by = ['Company','Job','Salary'], ascending = True, inplace = True )
emp_df_8a
# -

# #### ii. DataFrame.drop_duplicates(self, subset: Union[Hashable, Sequence[Hashable], NoneType] = None, keep: Union[str, bool] = 'first', inplace: bool = False, ignore_index: bool = False) → Union[ForwardRef('DataFrame'), NoneType]
#
# Return DataFrame with duplicate rows removed.
# Considering certain columns is optional. Indexes, including time indexes are ignored.
#
# 1. Parameters - subset column label or sequence of labels, optional : Only consider certain columns for identifying duplicates, by default use ALL of the COLUMNS.
#
# 2. keep - {‘first’, ‘last’, False}, default ‘first’ - Determines which duplicates (if any) to keep.
#
# first : Drop duplicates except for the first occurrence.
# last : Drop duplicates except for the last occurrence.
# False : Drop all duplicates.
#
# 3. inplace - bool, default False : Whether to drop duplicates in place or to return a copy.
#
# 4. ignore_index - bool, default False : If True, the resulting axis will be labeled 0, 1, …, n - 1.
# 5. Returns - DataFrame : DataFrame with duplicates removed or None if inplace=True.

# +
# Setup : DataFrame creation
emp_df_8b = emp_df_3a.copy()
emp_df_8b

emp_df_8b.drop_duplicates(['Job'], keep = 'first' , inplace = False)
emp_df_8b.drop_duplicates(['Job'], keep = 'last' , inplace = False)
emp_df_8b.drop_duplicates(['Job'], keep = False , inplace = False)


# -

# #### iiii.DataFrame.duplicated(self, subset: Union[Hashable, Sequence[Hashable], NoneType] = None, keep: Union[str, bool] = 'first') → 'Series'
# 0. Return boolean Series denoting duplicate rows.
#
# 1. Parameters - subset column label or sequence of labels, optional : Only consider certain columns for identifying duplicates, by default use all of the columns.
#
# 2. keep - {‘first’, ‘last’, False}, default ‘first’ : Determines which duplicates (if any) to mark.
#
# first : Mark duplicates as True except for the first occurrence.
# last : Mark duplicates as True except for the last occurrence.
# False : Mark all duplicates as True.
#
# 3. Returns - Series

# +
# Setup : DataFrame creation
emp_df_8c = emp_df_3a.copy()
emp_df_8c

# This return a boolean series indicating whether the row is a duplicate or not
emp_df_8c.duplicated(['Job'], keep = False)

# This returns the duplicated rows
emp_df_8c_dups = emp_df_8c[emp_df_8c.duplicated(['Job'], keep = False)]
emp_df_8c_dups

# Inclusion of TILDE (~), negate the boolean values and hence return the NON-duplicated rows
emp_df_8c_nodups = emp_df_8c[~emp_df_8c.duplicated(['Job'], keep = False)]
emp_df_8c_nodups
# -

