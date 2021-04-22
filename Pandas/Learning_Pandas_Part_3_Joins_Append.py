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
# ### https://www.linkedin.com/in/abhishek-kumar-442337b2/
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
          ['5','Anusha Yenduri','AIML', 'Data Scientist','M', 'Y', '01011989',  921000],
          ['6','Ritesh Srivastava','AIML', 'Data Engineer','M', 'Y', np.NaN, 785000]]

columns_name=['Emp_Id','Emp_Name','Department','Role','Gender', 'WFH Status', 'DOB', 'Salary']

emp_df = pd.DataFrame(salary,columns=columns_name)
emp_df
# -

# # 1. Concatenating dataframes vertically / Appending dataframes
#
# I ll take up 2 ways to do this.
#
#     i. df.append()
#     ii. pd.concat() - With concatenation, your datasets are just stitched together along an axis — either the row axis or column axis.

# ### i. df.append()

# +
detail_1 = ({'Id'   : [1,2,3,4],
             'Name' : ['A','B','C','D'],
             'Age'  : [21,22,20,24] })
detail_2 = ({'Id'   : [2,8,5],
             'Name' : ['Again','H','E'],
             'Age'  : [25,18,28],
             'City' : ['Pune','Panaji','Patna']})
detail_3 = ({'Id'   : [7,6],
             'Name' : ['G','F'],
             'Age'  : [34,30] })
df1 = pd.DataFrame(detail_1)
df2 = pd.DataFrame(detail_2)
df3 = pd.DataFrame(detail_3)
df1
df2
df3

# Multiple dataframe objects can be passed as a list
df_appended_1 = df1.append([df2,df3], sort=True) # sort=True/False - sorts the column names in Alphabetical order.
df_appended_1
df_appended_2 = df1.append([df2,df3], sort=False, ignore_index=True) # ignore_index= True creates a new index for the dataframe
df_appended_2
# -

df_appended_1 is df1

# ### Note : 
#     1. join= and keys= parameters are not available in df.append.
#     2. So, By default, ALL the columns are selected and index can be either retained or newly created.
#     3. It makes a full copy of the data, and that constantly reusing this function can create a significant performance hit. 

# ### ii. pd.concat(objs, axis=0, join='outer', sort='False', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, copy=True)
#
# pd.concat() is capable of concatenating dataframes either way longitudinal as well latitudinal.

# +
# Implementing the pd.concat() to behave similar to df.append()
# Default action of concat is vertical join/ append, as axis=0, by default.

df_appended_3 = pd.concat([df1,df2,df3], axis = 0, join = 'outer', sort= False)
df_appended_3

# +
df_appended_4 = pd.concat([df1,df2,df3], axis = 0, join = 'outer', sort = False , keys = ['a','b','c'], ignore_index = True, copy = True)
df_appended_4

# Note : Keys=a,b,c is passed, but still the keys are not assigned because the INDEXES are IGNORED. To create the keys, we need to retain the indexes.

# +
# The distinct keys are created, with keys= parameter and ignore_index=False
# join=inner considers only the common columns of all dataframes

df_appended_5 = pd.concat([df1,df2,df3], axis = 0, join = 'inner', sort = True , keys = ['a','b','c'], ignore_index = False, copy = True)
df_appended_5

# +
# The keys created above, can be used as filters.

df_appended_5.loc['b']
# -

# # 1.1 Appending Rows ( as Series )

# +
# Attention : Does not Work

s = pd.Series(['11', 'Eleven', 21])
s
df1
# appended_row = df1.append(s)
# appended_row = df1.append(s, ignore_index = True) # ignore_index = True fixes the error, but the output Dataframe is NOT DESIRED.
# appended_row
# -

s = pd.Series(['11', 'Eleven', 21], index = ['Id','Name', 'Age'])
s
df1
appended_row = df1.append(s, ignore_index = True)
appended_row

# +
# Set up

detail_1 = ({'Id'   : [1,2,3,4],
             'Name' : ['A','B','C','D'],
             'Age'  : [21,22,20,24] })
detail_2 = ({'Id'   : [1,2,5],
             'Sal'  : [100,200,500],
             'City' : ['Pune','Panaji',np.NaN]})

dfv_1 = pd.DataFrame(detail_1)
dfv_2 = pd.DataFrame(detail_2)
dfv_1
dfv_2

# +
# Does not make sense to me, as of now.

s2 = pd.Series(['_0', '_1', '_2', '_3'])

dfh_concat_s = pd.concat([dfv_1,dfv_2,s2,s2,s2], axis=0)
dfh_concat_s

# Uncomment and see the result , with rows have index name
# s3 = pd.Series(['_0', '_1', '_2', '_3'], index = ['Id','Name', 'Age','Sal'])

# dfh_concat_s = pd.concat([dfv_1,dfv_2,s3,s3,s3], axis=0, ignore_index = True)
# dfh_concat_s
# -

# # 2. Concatenating Dataframes horizontally
#
#     Using pd.concat(axis=1) - With concatenation, your datasets are just stitched together along an axis — either the row axis or column axis.

# ### pd.concat(objs, axis=1, join='outer', sort='False', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, copy=True)
#
# Parameter :
#
#     1. objs: This parameter takes any sequence (typically a list) of Series or DataFrame objects to be concatenated. You can also provide a dictionary. In this case, the keys will be used to construct a hierarchical index.
#
#     2. axis: Like in the other techniques, this represents the axis you will concatenate along. The default value is 0, which concatenates along the index (or row axis), while 1 concatenates along columns (vertically). You can also use the string values index or columns.
#
#     3. join: This is similar to the how parameter in the other techniques, but it only accepts the values inner or outer. The default value is outer, which preserves data, while inner would eliminate data that does not have a match in the other dataset.
#
#     4. ignore_index: This parameter takes a boolean (True or False) and defaults to False. If True, then the new combined dataset will not preserve the original index values in the axis specified in the axis parameter. This lets you have entirely new index values.
#
#     5. keys: This parameter allows you to construct a hierarchical index. One common use case is to have a new index while preserving the original indices so that you can tell which rows, for example, come from which original dataset.
#
#     6. copy: This parameter specifies whether you want to copy the source data. The default value is True. If the value is set to False, then Pandas won’t make copies of the source data.

# +
# Set up

detail_1 = ({'Id'   : [1,2,3,4],
             'Name' : ['A','B','C','D'],
             'Age'  : [21,22,20,24] })
detail_2 = ({'Id'   : [1,2,5],
             'Sal'  : [100,200,500],
             'City' : ['Pune','Panaji',np.NaN]})

dfh_1 = pd.DataFrame(detail_1, index = [5,6,7,1])
# dfh_1 = pd.DataFrame(detail_1)
dfh_2 = pd.DataFrame(detail_2)
dfh_1
dfh_2

# +
# The dataframes are concatenated horizontally based on INDEX

dfh_concat = pd.concat([dfh_1,dfh_2], axis=1, join = 'outer', ignore_index=False)
dfh_concat

# +
# With keys=a,b, the columns are labelled as 'a' and 'b' with ignore_index=False
# With join= parameter - is used to Set logic on the other axes 
# With join= inner, the common records are selected

dfh_concat = pd.concat([dfh_1,dfh_2], axis=1, join = 'inner', ignore_index=False ,keys = ['a','b'] , sort = False )
dfh_concat

# +
# ignore_index= True, column labels are Re-named.
# sort= True, sorts the records in ascending order

dfh_concat = pd.concat([dfh_1,dfh_2], axis=1, join = 'outer', ignore_index= True,sort = True )
dfh_concat
# -

# #### Note : With concatenation, your datasets are just stitched together along an axis — either the row axis or column axis.

# # 2.1 Appending Columns ( as Series)

# +
# Set up

detail_1 = ({'Id'   : [1,2,3,4],
             'Name' : ['A','B','C','D'],
             'Age'  : [21,22,20,24] })
detail_2 = ({'Id'   : [1,2,5],
             'Sal'  : [100,200,500],
             'City' : ['Pune','Panaji',np.NaN]})

dfh_1 = pd.DataFrame(detail_1)
dfh_2 = pd.DataFrame(detail_2)
dfh_1
dfh_2

# +
s2 = pd.Series(['_0', '_1', '_2', '_3'])

dfh_concat_s = pd.concat([dfh_1,dfh_2,s2,s2,s2], axis=1)
dfh_concat_s
# -

# # 3. Database-style DataFrame or named Series joining/merging
#
#     i. pd.merge()
#     ii. pd.join()

# ### i. pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True, indicator=False,validate=None)
#
#     1. how: This defines what kind of merge to make. It defaults to 'inner', but other possible options include 'outer', 'left', and 'right'.
#
#     2. on: Use this to tell merge() which columns or indices (also called key columns or key indices) you want to join on. This is optional. If it isn’t specified, and left_index and right_index (covered below) are False, then columns from the two DataFrames that share names will be used as join keys. If you use on, then the column or index you specify must be present in both objects.
#
#     3. left_on and right_on: Use either of these to specify a column or index that is present only in the left or right objects that you are merging. Both default to None.
#
#     4. left_index and right_index: Set these to True to use the index of the left or right objects to be merged. Both default to False.
#
#     5. suffixes: This is a tuple of strings to append to identical column names that are not merge keys. This allows you to keep track of the origins of columns with the same name.
#     
#     6. indicator: If True, a Categorical-type column called _merge will be added to the output object.Iindicator argument will also accept string arguments, in which case the indicator function will use the value of the passed string as the name for the indicator column.

# +
# Set up

detail_1 = ({'Id'   : [1,2,3,4],
             'Name' : ['A','B','C','D'],
             'Age'  : [21,22,20,24] })
detail_2 = ({'Id'   : [1,2,5],
             'Sal'  : [100,200,500],
             'City' : ['Pune','Panaji',np.NaN]})

df_mrg_1 = pd.DataFrame(detail_1)
df_mrg_2 = pd.DataFrame(detail_2)
df_mrg_1
df_mrg_2

# +
# how= inner, which tells the type of join
# if left_index and right_index are False, then columns from the two DataFrames that share names will be used as join keys
# So here, on = Id

data_merged = pd.merge(df_mrg_1,df_mrg_2)
data_merged

# +
# Set up

detail_1 = ({'Id'   : [1,2,3,4],
             'Name' : ['A','B','C','D'],
             'Age'  : [21,np.NaN,25,24] })
detail_2 = ({'Id'   : [1,2,5],
             'Age'  : [21,38,20],
             'Sal'  : [100,200,500],
             'City' : ['Pune','Panaji',np.NaN]})

df_mrg_1 = pd.DataFrame(detail_1)
df_mrg_2 = pd.DataFrame(detail_2)
df_mrg_1
df_mrg_2

# +
# There are Multiple things to observe here.
# 1. type of join, how= parameter states, here it is left join
# 2. on= parameter, defines the columns on which dataframes need to be joined, here ['Id', 'Age']
# 3a. suffixes= parameter, allows to differentiate the columns of different dataframes.
# 3b. Note: this won't add suffixes for columns which are passed in the 'on' parameter.
# 4. indicator = columns_name, states the presence of 'on' columns in dataframes being merged.

data_merged = pd.merge(df_mrg_1,df_mrg_2, how = 'left', on = ['Id'], suffixes=['_l', '_r'], indicator= 'Presence')
data_merged

# +
# Set up

detail_1 = ({'Id'   : [1,2,3,4],
             'Name' : ['A','B','C','D'],
             'Age'  : [21,np.NaN,25,24] })
detail_2 = ({'Id'   : [1,2,5],
             'Age'  : [21,38,20],
             'Sal'  : [100,200,500],
             'City' : ['Pune','Panaji',np.NaN]})

df_mrg_1 = pd.DataFrame(detail_1)
df_mrg_2 = pd.DataFrame(detail_2)
df_mrg_1
df_mrg_2

# +
# Now, the dataframes are merged based on INDEXes.
# Left dataframe Index is merged with Right dataframe Index

data_merged = pd.merge(df_mrg_1, df_mrg_2, left_index=True, right_index=True, how='outer')
data_merged

# +
# Now, the dataframes are merged by Joining key columns on an index.
# Left dataframe Index is merged with 'Id' from right dataframe.

data_merged = pd.merge(df_mrg_1, df_mrg_2, left_index=True, right_on='Id', how='inner')
data_merged
# -

# #### Note: There are more parameters of merge(). Please find them at [Pandas Documentation](#https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html).

# ### ii. DataFrame.join(self, other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
#
# Parameters:
#
#     1. other: This is the only required parameter. It defines the other DataFrame to join. You can also specify a list of DataFrames here, allowing you to combine a number of datasets in a single .join() call.
#
#     2. on: This parameter specifies an optional column or index name for the left DataFrame to join the other DataFrame’s index. If it’s set to None, which is the default, then the join will be index-on-index.
#
#     3. how: This has the same options as how from merge(). The difference is that it is index-based unless you also specify columns with on.
#
#     4. lsuffix and rsuffix: These are similar to suffixes in merge(). They specify a suffix to add to any overlapping columns but have no effect when passing a list of other DataFrames.
#
#     5. sort: Enable this to sort the resulting DataFrame by the join key.

# ### Note : 
#
#     While merge() is a module function, .join() is an object function that lives on the DataFrame. This enables you to specify only one DataFrame, which will join the DataFrame you call .join() on.

# +
# Set up

detail_1 = ({'Id'   : [1,2,3,4],
             'Name' : ['A','B','C','D'],
             'Age'  : [21,np.NaN,25,24] })
detail_2 = ({'Id'   : [1,2,5],
             'Age'  : [21,38,20],
             'Sal'  : [100,200,500],
             'City' : ['Pune','Panaji',np.NaN]})

df_mrg_1 = pd.DataFrame(detail_1)
df_mrg_2 = pd.DataFrame(detail_2)

df_mrg_1
df_mrg_2

# +
# Since the columns overlap, suffixes are required.Uncomment to see the error.
# df_mrg_1.join(df_mrg_2, how = 'inner', on = 'Id')

df_mrg_1.join(df_mrg_2, how = 'inner', on = 'Id', lsuffix = '_l', rsuffix = '_r' )
# -

# ### References : 
# #### 1. [Refer PDF](#https://drive.google.com/file/d/1Xe6Tm0fpBdIZJY96ZeojWEFtH5ZdqQXO/view?usp=drivesdk)
# #### 2. [Pandas Documentation](#https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)
# #### 3. [Real Python](#https://realpython.com/pandas-groupby/)
#


