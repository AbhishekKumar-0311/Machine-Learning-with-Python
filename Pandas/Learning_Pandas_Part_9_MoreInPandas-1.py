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

import numpy as np
import pandas as pd
sample = {
'col_a':['Houston,TX', 'Dallas,TX', 'Chicago,IL', 'Phoenix,AZ',      'San Diego,CA'],
'col_b':['62K-70K', '62K-70K', '69K-76K', '62K-72K', '71K-78K' ],
'col_c':['A','B','A','a','c'],
'col_d':['  1x', ' 1y', '2x  ', '1x', '1y  ']
}
df_sample = pd.DataFrame(sample)
df_sample

# # Functions discussed in this Notebook

# |Function	    							|Description																		|Part|
# |:-|:-|:-|
# |apply()									|Apply a function along an axis of the DataFrame.									|1|
# |applymap()									|Apply a function to a Dataframe elementwise. 										|1|
# |map()										|map() is used to substitute each value in a Series with another value.				|1|
# |transform()								|Call func on self producing a DataFrame with transformed values.					|1|
#
# |Function	    							|Description																		|Part|
# |:-|:-|:-|
# |pipe()										|Apply func(self, *args, **kwargs).													|2|
# |df.assign()								|Assign new columns to a DataFrame.													|2|
# |df.update()								|Modify in place using non-NA values from another DataFrame.						|2|
# |df.take									|Return the elements in the given positional indices along an axis.					|2|
# |df.truncate								|Truncate a Series or DataFrame before and after some index value.					|2|
#
# |Function	    							|Description																		|Part|
# |:-|:-|:-|
# |df.items									|Iterates over the DataFrame columns, returning a tuple with the column name and the content as a Series.|3|
# |df.iteritems								|Iterates over the DataFrame columns, returning a tuple with the column name and the content as a Series.|3|
# |df.iterrows								|Iterate over DataFrame rows as (index, Series) pairs.								|3|
# |df.itertuples								|Iterate over DataFrame rows as namedtuples.										|3|
#

# # Apply() , Applymap(), Map()

# - **https://medium.com/@evelynli_30748/map-apply-applymap-with-the-lambda-function-5e83028be759**
# - **https://towardsdatascience.com/introduction-to-pandas-apply-applymap-and-map-5d3e044e93ff**
# - **https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas**

# - **apply() is used to apply a function along an axis of the DataFrame or on values of Series.**
# - **applymap() is used to apply a function to a DataFrame elementwise.**
# - **map() is used to substitute each value in a Series with another value.**

# Setup Data
df = df_sample.copy()
df

# ### Problem 1 : Replacing 2nd word of col_a with 1st word of col_a

# +
# Replacing 2nd word of col_a with 1st word of col_a
dfp = df.copy()
#dfp

dfp['DupA'] = dfp['col_a']
dfp

x = dfp.col_a.str.split(',').str[0]

def func(row):
    return row['DupA'].replace(row['DupA'].split(',')[1], row['DupA'].split(',')[0])

# The Pandas apply() is used to apply a function along an axis of the DataFrame or on values of Series.
dfp['DupA'] = dfp.apply(func, axis = 1)

dfp

# d2= dfp.apply(func, axis = 1)

# d2
# -
# - Let’s take a look df.apply(func, axis=1)
#     - The first parameter func is a function.
#     - The second parameter axis is to specify which axis the function is applied to. 0 for applying the function to each column and 1 for applying the function to each row.
#         - Let me explain this process in a more intuitive way. The second parameter axis = 1 tells Pandas to use the row. So, the func is applied to each row and returns a new Series with the output of each row as value.

# ### Problem 2 : Creating a new column containing sepal length in mm
#
# - Using Map(), Column/Series Operation, Apply() with series

# we are going to use dataset Iris 
from sklearn.datasets import load_iris
data = load_iris()
features = pd.DataFrame(data = data['data'], columns= data ['feature_names'])
features.head() #glance at the data 


# +
#example : let's say, we would like to change the measurement of the sepal length from cm to mm, 
# this is what we can do with the map function and put a function call cm_to_mm inside. 
def cm_to_mm(cm):
    mm = cm * 10
    return mm

features['sl_mm1'] = features['sepal length (cm)'].map(cm_to_mm).head() #this way, we have used this function on this pandas series 

# -

features['sl_mm2'] = features['sepal length (cm)'] * 10
features.head()

features['sl_mm3'] = features['sepal length (cm)'].apply(lambda x : x*10)
features.head()

# ### Using apply() on 2 columns of  a dataframe, with axis = 0, by default

features[['sl_mm4','sl_mm5']] = features[['sepal length (cm)','sepal width (cm)']].apply(lambda x : x*10)
features.head()

# ### Using apply() on 2 columns of  a dataframe, with axis = 1 i.e, taking each row for operation
#

# - with Lambda function

features['sl_mm45'] = features[['sl_mm4','sl_mm5']].apply(lambda x : x['sl_mm4']+x['sl_mm5'], axis=1)
features.head()


# - with User defined function

# +
def sum(x):
    return x['sl_mm4']+x['sl_mm5']

features['sl_mm45'] = features[['sl_mm4','sl_mm5']].apply(sum, axis=1)
features.head()


# -

# ### Extra parameters in Map() does not work

# +
def label(element, x):
    if element > x:
        return 'High'
    else:
        return 'Low'
    
# features['sl_mm45'].map(label, x = 32) # Does not work


# +
def label(element):
    if element > 32:
        return 'High'
    else:
        return 'Low'

features['sl_mm45'].map(label)
# -



# ## Applymap()
#
# ### The applymap() method works on the entire pandas data frame where the input function is applied to every element individually. In other words, applymap() is appy() + map()!









# ### Comparing map, applymap and apply: Context Matters
#
# - First major difference: **DEFINITION**
#
#     - ```map``` is defined on Series ONLY
#     - ```applymap``` is defined on DataFrames ONLY
#     - ```apply``` is defined on BOTH
#
# - Second major difference: **INPUT ARGUMENT**
#
#     - ```map``` accepts ```dicts```, ```Series```, or callable
#     - ```applymap``` and ```apply``` accept callables only
#
# - Third major difference: **BEHAVIOR**
#
#     - ```map``` is elementwise for Series
#     - ```applymap``` is elementwise for DataFrames
#     - ```apply``` also works elementwise but is suited to more complex operations and aggregation. The behaviour and return value depends on the function.
#
# - Fourth major difference (the most important one): **USE CASE**
#
#     - ```map``` is meant for mapping values from one domain to another, so is optimised for performance (e.g., ```df['A'].map({1:'a', 2:'b', 3:'c'}))```
#     - ```applymap``` is good for elementwise transformations across multiple rows/columns (e.g., ```df[['A', 'B', 'C']].applymap(str.strip))```
#     - ```apply``` is for applying any function that cannot be vectorised (e.g., ```df['sentences'].apply(nltk.sent_tokenize))```
#     
# ### Summarising
#
# ![image.png](attachment:image.png)
#
# Footnotes
#
# 1. ```map``` when passed a dictionary/Series will map elements based on the keys in that dictionary/Series. Missing values will be recorded as NaN in the output.
# 2. ```applymap``` in more recent versions has been optimised for some operations. You will find ```applymap``` slightly faster than ```apply``` in some cases. My suggestion is to test them both and use whatever works better.
#
# 3. ```map``` is optimised for elementwise mappings and transformation. Operations that involve dictionaries or Series will enable pandas to use faster code paths for better performance.
#
# 4. ```Series.apply``` returns a scalar for aggregating operations, Series otherwise. Similarly for ```DataFrame.apply```. Note that ```apply``` also has fastpaths when called with certain NumPy functions such as ```mean```, ```sum```, etc.
#
# - **https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas**



# # Transform()

# - **https://towardsdatascience.com/when-to-use-pandas-transform-function-df8861aa0dcf**
# - **https://pbpython.com/pandas_transform.html**
# - **https://www.analyticsvidhya.com/blog/2020/03/understanding-transform-function-python/**

# 1. Transforming values
# 2. Combining groupby() results
# 3. Filtering data
# 4. Handling missing value at the group level

# ## 1. Transform values

# ### A function

df = pd.DataFrame({'A': [1,2,3], 'B': [10,20,30] })
df


# +
def plus_10(x):
    return x+10

df.transform(plus_10)
# -

df.transform(lambda x: x+10)

# ### A string function

df.transform('sqrt')

# ### A list of functions

df.transform([np.sqrt, np.exp])

# ### A dict of axis labels -> functions

df.transform({
    'A': np.sqrt,
    'B': np.exp,
})

# ## 2. Combining groupby results

# a dataset about a restaurant chain
df = pd.DataFrame({
  'restaurant_id': [101,102,103,104,105,106,107],
  'address': ['A','B','C','D', 'E', 'F', 'G'],
  'city': ['London','London','London','Oxford','Oxford', 'Durham', 'Durham'],
  'sales': [10,500,48,12,21,22,14]
})
df


# ### Soluton one: `groupby()`, `apply()`, and `merge()`

# +
# Step 1: groupby and sum
def sum(col):
    return col.sum()

# Call the user defined sum function - by default axis=0, which means it applies on a column ( a series)
city_sales = df.groupby('city')['sales'].apply(sum).rename('city_total_sales').reset_index()
city_sales
# -

# Step 1: The Pandas sum equivalent 
city_sales = df.groupby('city')['sales'].sum().rename('city_total_sales').reset_index()
city_sales

# Step 2: merge
df_new = pd.merge(df, city_sales, how='left')
df_new

# +
# Step 3
df_new['pct'] = df_new['sales'] / df_new['city_total_sales']
df_new['pct'] = df_new['pct'].apply(lambda x: format(x, '.2%'))

df_new
# -

# ### Solution 2: `groupby()` and `transform()`

# Step 1
df['city_total_sales'] = df.groupby('city')['sales'].transform('sum')
df

# Step 2
df['pct'] = df['sales'] / df['city_total_sales']
df['pct'] = df['pct'].apply(lambda x: format(x, '.2%'))
df

# ## 3. Filtering data

df[df.groupby('city')['sales'].transform('sum') > 40]

# ## 4. Handling missing values at the group level

df = pd.DataFrame({
    'name': ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'value': [1, np.nan, np.nan, 2,8,2,np.nan, 3]
})
df

df.groupby('name')['value'].mean()

df['value'] = df.groupby('name').transform(lambda x: x.fillna(x.mean()))
df

# ## Difference between apply() and transform() in Pandas
#
# - 3 main differences
#
#     1. `transform()` can take a function, a string function, a list of functions, and a dict. However, `apply()` is only allowed a function.
#     2. `transform()` cannot produce aggregated results
#     3. `apply()` works with multiple Series at a time. However, `transform()` is only allowed to work with a single Series at a time.
#     
# - **https://towardsdatascience.com/difference-between-apply-and-transform-in-pandas-242e5cf32705**
# - **https://www.analyticsvidhya.com/blog/2020/03/understanding-transform-function-python/**

# ## 1 Manipulating values

df = pd.DataFrame({'A': [1,2,3], 'B': [10,20,30] })


def plus_10(x):
    return x+10


# #### For the entire DataFrame

df.apply(plus_10)

df.transform(plus_10)

## lambda equivalent
df.apply(lambda x: x+10)

## lambda equivalent
df.transform(lambda x: x+10)

# #### For a single column

df['B_ap'] = df['B'].apply(plus_10)
df

df['B_tr'] = df['B'].transform(plus_10)
df

# ### Difference

# 3 main differences
# 1. `transform()` can take a function, a string function, a list of functions, and a dict. However, `apply()` is only allowed a function.
# 2. `transform()` cannot produce aggregated results
# 3. `apply()` works with multiple Series at a time. However, `transform()` is only allowed to work with a single Series at a time.

df = pd.DataFrame({'A': [1,2,3], 'B': [10,20,30] })

# **1. `transform()` can takes a function, a string function, a list of functions, and a dict. However, `apply()` is only allowed a function.**

# A string function
df.transform('sqrt')

# A list of functions
df.transform([np.sqrt, np.exp])

# +
# A dict of axis labels -> function
df.transform({
    'A': np.sqrt,
    'B': np.exp,
})

df[['A1','B1']] = df.transform({
    'A': np.sqrt,
    'B': np.exp,
})

df
# -

# **2. `transform()` cannot produce aggregated results**

# This is working for apply()
df.apply(lambda x:x.sum())


# - **This feature is not possible in the Transform function. This just manipulates a single row or column based on axis value and doesn’t manipulate a whole dataframe. So, we can use either Apply or the Transform function depending on the requirement.**

# +
## but getting error with transform()
# Uncomment to check

# df.transform(lambda x:x.sum())
# -

# ![image.png](attachment:image.png)

# **3. `apply()` works with multiple Series at a time. However, `transform()` is only allowed to work with a single Series at a time.**

def subtract_two(x):
    return x['B'] - x['A']


# Working for apply with axis=1
df['diff1'] = df.apply(subtract_two, axis=1)
df

# - **This feature is not possible in the Transform function. This just manipulates a single row or column based on axis value and doesn’t manipulate a whole dataframe. So, we can use either Apply or the Transform function depending on the requirement.**

# +
# Getting error when trying the same with transform
# Uncomment to check
# df['diff2'] =  df.transform(subtract_two, axis=1)
# df
# -

# ![image.png](attachment:image.png)

# apply() works fine with lambda expression
df.apply(lambda x: x['B'] - x['A'], axis=1)

# +
# Same error when using lambda expression
# Uncomment to see error

# df.transform(lambda x: x['B'] - x['A'], axis=1)
# -

# ![image.png](attachment:image.png)

# ## 2 In conjunction with groupby()

df = pd.DataFrame({
    'key': ['a','b','c'] * 3,
    'A': np.arange(9),
    'B': [1,2,3] * 3,
})
df


# 2 differences
# 1. `transform()` returns a Series that has the same length as the input
# 2. `apply()` works with multiple Series at a time. However, `transform()` is only allowed to work with a single Series at a time.

# **1. `transform()` returns a Series that has the same length as the input**

def group_sum(x):
    return x.sum()


gr_data_ap = df.groupby('key')['A'].apply(group_sum)
gr_data_ap

gr_data_tr = df.groupby('key')['A'].transform(group_sum)
gr_data_tr


# **2. `apply()` works with multiple Series at a time. However, `transform()` is only allowed to work with a single Series at a time.**

def subtract_two(x):
    return x['B'] - x['A']


df.groupby('key').apply(subtract_two)

# +
## Getting error

# Uncommenet to see error
# df.groupby('key').transform(subtract_two)
# -


