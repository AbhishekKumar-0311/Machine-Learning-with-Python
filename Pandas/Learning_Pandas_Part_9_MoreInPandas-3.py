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

# # Functions discussed in this Notebook - Part 3

# |Function	    							|Description																		|Part|
# |:-|:-|:-|
# |apply()									|Apply a function along an axis of the DataFrame.									|1|
# |applymap()									|Apply a function to a Dataframe elementwise. 										|1|
# |map()										|map() is used to substitute each value in a Series with another value.				|1|
# |transform()								|Call func on self producing a DataFrame with transformed values.					|1|
#
# |Function	    							|Description																		|Part|
# |:-|:-|:-|
# |df.assign()								|Assign new columns to a DataFrame.													|2|
# |pipe()										|Apply func(self, *args, **kwargs).													|2|
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

# ## Description

# This Part is about Iteration over Dataframe, be it rows or columns.
#
# The explicit looping is Not as Efficient as the Implicit techniques.
#
# The following blogs give a complete idea about looping Dataframes.

# ### 1. https://www.dataindependent.com/pandas/pandas-iterate-over-rows/
# ### 2. https://realpython.com/fast-flexible-pandas/
# ### 3. https://stackoverflow.com/questions/24870953/does-pandas-iterrows-have-performance-issues/24871316#24871316

# ## Summary
#
# - **Use ```vectorized operations```: Pandas methods and functions with no for-loops.**
# - **Use the ```.apply()``` method with a callable.**
# - **Use ```.itertuples()```: iterate over DataFrame rows as namedtuples from Python’s collections module.**
# - **Use ```.iterrows()```: iterate over DataFrame rows as (index, pd.Series) pairs. While a Pandas Series is a flexible data structure, it can be costly to construct each row into a Series and then access it.**
# - **Use “element-by-element” for loops, updating each cell or row one at a time with ```df.loc``` or ```df.iloc```. (Or, .at/.iat for fast scalar access.)**







# # What's More..?? Upcoming HDFStore

# ## Prevent Reprocessing with HDFStore

# Pandas has a built-in solution for this which uses HDF5 , a high-performance storage format designed specifically for storing tabular arrays of data. Pandas’ HDFStore class allows you to store your DataFrame in an HDF5 file so that it can be accessed efficiently, while still retaining column types and other metadata. It is a dictionary-like class, so you can read and write just as you would for a Python dict object.
#
# Here’s how you would go about storing your pre-processed DataFrame, df, in an HDF5 file

# +
# Create storage object with filename `processed_data`
data_store = pd.HDFStore('processed_data.h5')

# Put DataFrame into the object setting the key as 'preprocessed_df'
data_store['preprocessed_df'] = emp_df
data_store.close()

# +
# Access data store
data_store = pd.HDFStore('processed_data.h5')

# Retrieve data using key
preprocessed_emp_df = data_store['preprocessed_df']
data_store.close()
# -

preprocessed_emp_df


