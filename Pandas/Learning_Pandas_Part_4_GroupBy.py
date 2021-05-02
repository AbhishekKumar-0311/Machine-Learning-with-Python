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

# +
# Setup : DataFrame creation

salary = [['1','Abhishek Kumar','AIML', 'Machine Learning Engineer','M', 'Y', '04051990', 1121000],
          ['2','Arjun Kumar','DM', 'Tech Lead','M', 'Y', '09031992', 109000],
          ['3','Vivek Raj','DM', 'Devops Engineer','M', 'N', np.NaN , 827000],
          ['4','Mika Singh','DM', 'Data Analyst','F', 'Y', '15101991',  np.NaN],
          ['5','Anusha Yenduri','AIML', 'Data Scientist','F', 'Y', '01011989',  921000],
          ['6','Ritesh Srivastava','AIML', 'Data Engineer','M', 'Y', np.NaN, 785000]]

columns_name=['Emp_Id','Emp_Name','Department','Role','Gender', 'WFH Status', 'DOB', 'Salary']

emp_df = pd.DataFrame(salary,columns=columns_name)
emp_df
# -

# # 1. Group By: Split-Apply-Combine
#
#
#     i. df.groupby()
#     ii. .apply() , .agg(), .filter()
#     iii. 

emp_df_1 = emp_df.copy()
emp_df_1

grouped_1 = emp_df_1.groupby('Department')
grouped_1

# ## 1.1 Meta Methods
#
#     Meta methods are less concerned with the original object on which .groupby() is called.
#     Mainly provide high-level information such as the number of groups and indices of those groups.

grouped_1.groups

grouped_1.get_group('DM')

grouped_1.indices

grouped_1.ndim

grouped_1.ngroups

# Assign this to a new variable. This will assign a number to each group
grouped_1.ngroup()

grouped_1.dtypes

# +
#for i in range(2):
#    grouped_1.__iter__()
# -

grouped_1.size()

len(grouped_1)

# ## 1.2 Filter Methods
#
#     Filter methods return a subset of the original DataFrame. 
#     Most common is .filter() to drop entire groups based on some comparative statistic about that group and its sub-table. 
#     There are a number of methods that exclude particular rows from each group.

grouped_2 = emp_df_1.groupby('Department')
grouped_2

grouped_2.first()

grouped_2.last()

grouped_2.head(2)

grouped_2.tail(1)

# +
# Take the nth row from each group if n is an int, or a subset of rows if n is a list of ints.

grouped_2.nth(2)

grouped_2.nth([0,2])

# +
# we are selecting the 0th and 2nd rows, not rows whose indices equal 0 and 2.

grouped_2.take([0,2])

# +
grouped_1 = emp_df_1.groupby('Department', as_index=False)
grouped_1

# The argument of filter must be a function that, applied to the group as a whole, returns True or False.

grouped_1.filter(lambda x: max(x['Salary']) >= 1121000.0)
# -

# ### Transform

# +
# Using transform to get boolean values and then passing this boolean value to the dataframe to get the correct record
# NOT WORKING AS EXPECTED

emp_df_1['PctSalary'] = grouped_1['Salary'].transform('max')
emp_df_1

# +
# The argument of filter must be a function that, applied to the group as a whole, returns True or False.

grouped_1.filter(lambda x: len(x['Emp_Id']) >=3)

# +
# The argument of filter must be a function that, applied to the group as a whole, returns True or False.

grouped_2.filter(lambda x: sum(x['Salary']) >= 950000)
# -



# ## 1.3 Aggregation Methods
# - .agg()
#
#     Aggregation methods (also called reduction methods) “smush” many data points into an aggregated statistic about those data points.
#     An example is to take the sum, mean, or median of 10 numbers, where the result is just a single number. 

grouped_3 = emp_df_1.groupby('Department')
grouped_3

# +
# grouped_3.agg(np.sum)

grouped_3.agg('sum')
# -

grouped_3.agg('mean')

# ### + Applying multiple functions at once

x= grouped_3.agg(['max','mean', 'min'])
x

# ### - End

# ### + Analysing the aggregated result dataframe

x.ndim

x.size

x.shape

len(x)

x.iloc[:,2:]

x.columns
x.columns[0]

x.index
x.index[0]

# ### - End

# +
# as_index = False does not create the groupby columns as Indexes

grouped_3a = emp_df_1.groupby(['Department','Gender'], as_index = False)
grouped_3a
# -

grouped_3a.agg('sum')
grouped_3a['Salary'].agg(['sum'])

# +
# We can also use the reset_index DataFrame function to achieve the same result as the column names are stored in the resulting MultiIndex

emp_df_1.groupby(['Department','Gender']).sum().reset_index()
# -

grouped_3a.size()
grouped_3a.size().reset_index()

grouped_3a.describe()

grouped_3a.aggregate('count')
grouped_3a.count()
grouped_3a.agg(lambda x: x.count())

grouped_3a['Salary'].aggregate('count')
grouped_3a['Salary'].count()
grouped_3a['Salary'].agg(lambda x: x.count())

# #### Note: The aggregating functions above will exclude NA values. 

# ### Renaming column labels
#
#     i. .rename()
#     ii. Named Aggregation

# #### i. .rename()

grouped_3b = emp_df_1.groupby(['Department','Gender'])
grouped_3b

grouped_3b.agg(['min','max','mean'])
grouped_3b.agg(['min','max','mean']).rename(columns = { 'min' : 'Least', 'max': 'Most', 'mean':'Avg'})

# #### ii. NamedAggregation
#
#     To support column-specific aggregation with control over the output column names, pandas accepts the special syntax in GroupBy.agg(), known as “named aggregation”, where
#
#     i. The keywords are the output column names
#
#     ii. The values are tuples whose first element is the column to select and the second element is the aggregation to apply to that column.
#     
#     iii. Pandas provides the pandas.NamedAgg namedtuple with the fields ['column', 'aggfunc'] to make it clearer what the arguments are. As usual, the aggregation can be a callable or a string alias.

# +
# Named Tuple

grouped_3b.agg( Max_Sal = pd.NamedAgg( column = 'Salary' , aggfunc = 'max'),
                Min_Sal = pd.NamedAgg( column = 'Salary' , aggfunc = 'min'),
                Avg_Sal = pd.NamedAgg( column = 'Salary' , aggfunc = 'mean'))


# Plain Tuple
# Also, the index is reset here.

grouped_3b.agg( Max_Sal = pd.NamedAgg( 'Salary' ,  'max'),
                Min_Id = pd.NamedAgg( 'Emp_Id' ,  'min'),
                Avg_Sal = pd.NamedAgg( 'Salary' ,  'mean')).reset_index()

# -

# ### Applying different functions to DataFrame columns
#
#     By passing a dict to aggregate we can apply a different aggregation to the columns of a DataFrame

# +
grouped_3b.agg({ 'Salary' : lambda x: np.std(x, ddof=1)})

# index on Groupby columns is also reset.
grouped_3b.agg({ 'Salary' : 'mean', 'Role' : 'sum'}).reset_index()
# -

# ## 1.4 Transformation
# - .transform()
#
#     Transformation methods return a DataFrame with the same shape and indices as the original, but with different values. 
#     With both aggregation & filter methods, the resulting DataFrame will commonly be smaller in size than the input DF. 
#     This is not true of a transformation, which transforms individual values themselves but retains d shape of the original DataFrame.

grouped_3c = emp_df_1.groupby(['Department'])
grouped_3c.count()

# +
# Here i have not created a new column
# But a new column can be created 

transformed = grouped_3c.transform(lambda x : x.fillna(x.mean()))
transformed
# -

grouped_trans = transformed.groupby(level=0)
grouped_trans.count()

# ### + Window and resample operations
#
#     i. rolling()
#     ii. expanding()
#     iii. resample()

df_re = pd.DataFrame({'A': [1] * 10 + [5] * 10,
                      'B': np.arange(20)})
df_re.head()
df_re.tail()

# +
# This will apply the rolling() method on the samples of the column B based on the groups of column A.

df_re.groupby('A').rolling(4).B.sum()

# +
# The expanding() method will accumulate a given operation (sum() in the example) for all the members of each particular group.

df_re.groupby('A').expanding().B.sum()

# +
# ReSampling is not yet covered...
# -
# ## Iteration 2

df1 = pd.DataFrame({'id': [1,2],
                   'name': ['a','b'],
                   'prem1' : [100,280],
                   'prem2' : [np.NaN,180],
                   'prem3' : [300,np.NaN],
                   'disc1' : [20,40],
                   'disc2' : [np.NaN,30],
                   'disc3' : [50,np.NaN],})
df1

df1_melted = pd.wide_to_long(df1, i=['id','name'], j='month', stubnames=['prem','disc'])
df_long = df1_melted.reset_index()

df_long

df_long.groupby('id').min()

df_long.groupby('id').max()

df_long.groupby('id').first()

df_long.groupby('id').last()

df_long.groupby('id').head(2)

df_long.groupby('id').tail(1)

df_long2 = df_long.sort_values(['id','prem'])

df_long2.groupby('id').head(2)

df_long2.groupby('id').tail(1)

# ## TRANSFORM
#
# https://pbpython.com/pandas_transform.html

df_long['flag'] = df_long.groupby('id')['prem'].transform(lambda x : x == x.max())
df_long

# https://www.analyticsvidhya.com/blog/2020/03/understanding-transform-function-python/



# ## Creating running totals with cumsum( )

# +
d = {"salesperson":["Nico", "Carlos", "Juan", "Nico", "Nico", "Juan", "Maria", "Carlos"], "item":[10, 120, 130, 200, 300, 550, 12.3, 200]}
df = pd.DataFrame(d)
df

df["running_total"] = df["item"].cumsum()
df["running_total_by_person"] = df.groupby("salesperson")["item"].cumsum()
df
# -

# ## Calculate running count with groups using cumcount() + 1

# +
d = {"salesperson":["Nico", "Carlos", "Juan", "Nico", "Nico", "Juan", "Maria", "Carlos"], "item":["Car", "Truck", "Car", "Truck", "cAr", "Car", "Truck", "Moto"]}
df = pd.DataFrame(d)
df

# Fixing columns
df["salesperson"] = df["salesperson"].str.title()
df["item"] = df["item"].str.title()

df["count_by_person"] = df.groupby("salesperson").cumcount() + 1
df["count_by_item"] = df.groupby("item").cumcount() + 1
df["count_by_both"] = df.groupby(["salesperson","item"]).cumcount() + 1
df
# -

# Creating a new dataframe
emp_df3 = emp_df.copy()

emp_df3.groupby('Department').first()
emp_df3.groupby('Department').head(1)

emp_df3.groupby('Department').last()
emp_df3.groupby('Department').tail(1)

emp_df3.sort_values(['Department','Emp_Name'], ascending=True).groupby('Department').last()
emp_df3.sort_values(['Department','Emp_Name'], ascending=False).groupby('Department').tail(1)

emp_df3.sort_values(['Department','Salary'], ascending=False).groupby('Department').last()
emp_df3.sort_values(['Department','Salary'], ascending=False).groupby('Department').tail(1)

# ## To generate ranking within each group
# - method = 'first' / 'dense' / 'min' / 'max' / 'average'
# - ascending = True/False
# - pct = True

# ### Example 1

emp_df3.dtypes
emp_df3['Salary'] = emp_df3['Salary'].astype('float')

# Rank() does not work when rank is done on NON-Numeric column
emp_df3['default_rank2'] = emp_df3.groupby('Department')[['Salary']].rank(ascending=False)
emp_df3

emp_df3['default_rank'] = emp_df3['Salary'].rank()
emp_df3

# ### Example 2

data = {'close_date': ["2012-08-01", "2012-08-01", "2012-08-01", "2012-08-02", "2012-08-03", "2012-08-04", "2012-08-05", "2012-08-07"],
        'seller_name': ["Lara", "Julia", "Julia", "Emily", "Julia", "Lara", "Julia", "Julia"]
       }
df = pd.DataFrame(data)

df['close_date'] = pd.to_datetime(df['close_date'])

df['rank_seller_by_close_date'] = df.groupby('seller_name')['close_date'].rank(method='first')



# ## Other functions

# +

emp_df3['default_rank3'] = emp_df3.groupby('Department')['default_rank'].bfill()
emp_df3
# -

emp_df3.sort_values(['Department','Salary'], ascending=True).groupby('Department')['Salary'].nth(0).to_frame().reset_index()
# emp_df3

emp_df3.groupby('Department')['Role'].unique()

emp_df3.groupby('Department')['Role'].nunique()

ods = emp_df3.groupby('Department', as_index = False)
ods['Role'].count()

emp_df3.groupby('Department', as_index = False)['Role'].size()

emp_df3.groupby('Department')['Role'].describe()

emp_df3.groupby('Department')['Gender'].value_counts()

emp_df3.groupby('Department')['Salary'].nlargest()

emp_df3.groupby('Department')['Salary'].nsmallest()

emp_df3.groupby('Department')['Salary'].sum()

# as_index helps to create a dataframe
emp_df3.groupby('Department', as_index=False)['Salary'].min()

emp_df3.groupby('Department')['Salary'].max()

emp_df3.groupby('Department')['Salary'].mean()

emp_df3

# ## Cumulative sum within each group using CUMSUM( )

emp_df3['Salary'].fillna(0, inplace=True)
emp_df3

emp_df3['cum_sal'] = emp_df3.groupby('Department')['Salary'].cumsum()
emp_df3

# ## To generate a sequential rownumber using CUMCOUNT() + 1

emp_df3['Count'] = emp_df3.sort_values(['Department','Emp_Name'], ascending=True).groupby('Department')['Emp_Name'].cumcount()+1
emp_df3.sort_values(['Department','Emp_Name'], ascending=True, inplace=True)
emp_df3

tmp = emp_df3.groupby('Department')['Emp_Name'].cumcount().reset_index()
tmp
tmp.rename(columns={tmp.columns[-1]:'new'},inplace=True)
tmp

emp_df3 = pd.merge(emp_df3,tmp, left_index=True, right_index=True).drop('index', axis=1)
emp_df3

# ## LAG (+n) / LEAD (-n) functionality
# ## To retrieve previous  (+n) /ahead (-n) values using SHIFT(n / -n)
# - shift(n) : LAG 
# - shift(-n) : LEAD

emp_df3.sort_values(['Department','Salary'],inplace=True)
emp_df3['PrevSal'] = emp_df3.groupby('Department')['Salary'].shift(1)
emp_df3

# ## Retain the last filled value to fill the NaN cells
# ## Using FILLNA( method = 'bfill' / 'ffill' )
#
# ### bfill - backward fill : Go Backward and fill the empty cell
# ### ffill  - forward fill    : Go Forward and fill the empty cell
#

emp_df3

emp_df3.loc[emp_df3.Emp_Id.isin( ['4','6']), 'PrevSal'] = np.NaN
emp_df3.sort_values(['Department','Emp_Name'], inplace = True)
emp_df3

emp_df3['ForwardFilledPrevSal'] = emp_df3.groupby('Department')['PrevSal'].fillna(method = 'ffill')
emp_df3

emp_df3['BackwardFilledPrevSal'] = emp_df3.groupby('Department')['PrevSal'].fillna(method = 'bfill')
emp_df3

# ## filling-missing-values-by-mean-in-each-group

emp_df3['MeanFilledPrevSal'] = emp_df3.groupby('Department')['BackwardFilledPrevSal'].transform(lambda x: x.fillna(x.mean()))
emp_df3

# ### References:
#
# #### 1. [Pandas Documentation](#https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)
# #### 2. [Real Python](#https://realpython.com/pandas-groupby/)
# #### 3. [TDS - Window Functions](#https://towardsdatascience.com/window-functions-in-pandas-eaece0421f7)


