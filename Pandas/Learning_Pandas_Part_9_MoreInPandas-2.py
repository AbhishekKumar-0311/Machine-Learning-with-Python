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
import seaborn as sns
import sys

# +
# To get multiple outputs in the same cell

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# %matplotlib inline
# -

# # Data Preparation

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

# # Functions discussed in this Notebook - Part 2

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



# +
# Data prep

df = df_sample.copy();
df
# -

df.values

df.col_a.tolist()



# ## Assign()
# - DataFrame.assign(**kwargs)[source]
#     - Assign new columns to a DataFrame.
#
# - Parameters
#     - **kwargsdict of {str: callable or Series}
#         - The column names are keywords. If the values are callable, they are computed on the DataFrame and assigned to the new columns. The callable must not change input DataFrame (though pandas doesn’t check it). If the values are not callable, (e.g. a Series, scalar, or array), they are simply assigned.
#
# - Returns : DataFrame
#     - A **new DataFrame** with the **new columns in addition to all the existing columns**.
#     
# - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html
# - https://towardsdatascience.com/using-pandas-method-chaining-to-improve-code-readability-d8517c5626ac

# +
# emp_df.dtypes
# -

empdf = emp_df.copy()
empdf

empdf = empdf.assign(NewSal1 = lambda x : x.Salary*1.1)
empdf

empdf = empdf.assign(NewSal2 = empdf.Salary*1.1)
empdf

# ### **We can create multiple columns within the same assign where one of the columns depends on another one defined within the same assign:**

# +
# empdf.assign(NewSal3 = empdf.NewSal1 + empdf.NewSal2,
#              NewSal4 = empdf.NewSal3 + empdf.NewSal3)
# -

# ![image.png](attachment:image.png)

# ### **But it does not work like this. We need to create the SECOND NEW Column using LAMBDA function.**
# - i.e, the dependent columns should be created with lambda expressions

empdf.assign(NewSal3 = lambda x : x.NewSal1 + x.NewSal2,
             NewSal4 = lambda x : x.NewSal3 + x.NewSal3)

empdf.assign(NewSal33 = empdf.NewSal1 + empdf.NewSal2,
             NewSal44 = lambda x : x.NewSal33 + x.NewSal33)

empdf.assign(NewSal33 = empdf.NewSal1 + empdf.NewSal2,
             NewSal44 = lambda x : x.NewSal33 + x.NewSal33, NewSal55 = lambda x : x.NewSal44 + x.NewSal44)


# ## PIPE
# - DataFrame.pipe(func, *args, **kwargs)[source]
#     - Apply func(self, *args, **kwargs).
# - Parameters :
#     - func function
#         - Function to apply to the Series/DataFrame. args, and kwargs are passed into func. Alternatively a (callable, data_keyword) tuple where data_keyword is a string indicating the keyword of callable that expects the Series/DataFrame.
#
#     - args iterable, optional
#         - Positional arguments passed into func.
#
#     - kwargs mapping, optional
#         - A dictionary of keyword arguments passed into func.
#
# - Returns : objectthe return type of func.
#
# - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html
# - https://towardsdatascience.com/using-pandas-method-chaining-to-improve-code-readability-d8517c5626ac
# - https://towardsdatascience.com/using-pandas-pipe-function-to-improve-code-readability-96d66abfaf8

# +
# I have taken up the titanic dataset for this case

def load_data():
    return pd.read_csv('./titanic.csv')
df = load_data()
df.head()


# -

# ### Tasks
# Suppose we have been asked to work on the following tasks
#
# 1. Split Name into first name and second name
# 2. For Sex, substitute value male with M and female with F
# 3. Replace the missing Age with some form of imputation
# 4. Convert ages to groups of age ranges: ≤12, Teen (≤18), Adult (≤60), and Older (>60).
#
# - Let’s go ahead and use ```pipe()``` to accomplish them step by step,
#
#

# ### 1. Split Name into first name and second name

def split_name(x_df):
    def split_name_series(string):
        firstName, secondName=string.split(', ')
#         print(type(firstName))
        c =  pd.Series(
            (firstName, secondName),
            index='firstName secondName'.split()
        )
#         print(c)
#         print(type(c))
        return c
    # Select the Name column and apply a function
    res=x_df['Name'].apply(split_name_series)
#     print(type(res))
#     print(res)
    x_df[res.columns]=res
#     print(x_df)
    return x_df


res=(
    load_data()
    .pipe(split_name)
)
res.head()


# ### 2. For Sex, substitute value male with M and female with F

def substitute_sex(x_df):
    mapping={'male':'M','female':'F'}
    x_df['Sex']=df['Sex'].map(mapping)
    return x_df


res=(
    load_data()
    .pipe(split_name)
    .pipe(substitute_sex)
)
res.head()

# ### 3. Replace the missing Age with some form of imputation

sns.boxplot(x='Pclass',
            y='Age',
            data=df,
            palette='winter')


pclass_age_map = {
  1: 37,
  2: 29,
  3: 24,
}
def replace_age_na(x_df, fill_map):
    cond=x_df['Age'].isna() 
    res=x_df.loc[cond,'Pclass'].map(fill_map)
    x_df.loc[cond,'Age']=res
    return x_df


res=(
    load_data()
    .pipe(split_name)
    .pipe(substitute_sex)
    .pipe(replace_age_na, pclass_age_map)
)
res.head()

sns.heatmap(res.isnull(), 
            yticklabels=False, 
            cbar=False, 
            cmap='viridis')


# ### 4. Convert ages to groups of age ranges: ≤12, Teen (≤18), Adult (≤60), and Older (>60)

def create_age_group(x_df):
    bins=[0, 13, 19, 61, sys.maxsize]
    labels=['<12', 'Teen', 'Adult', 'Older']
    ageGroup=pd.cut(x_df['Age'], bins=bins, labels=labels)
    x_df['ageGroup']=ageGroup
    return x_df


res=(
    load_data()
    .pipe(split_name)
    .pipe(substitute_sex)
    .pipe(replace_age_na, pclass_age_map)
    .pipe(create_age_group)
)
res.head()

# ### More examples :
# ### https://www.kdnuggets.com/2021/01/cleaner-data-analysis-pandas-pipes.html

# ## Update()

# - DataFrame.update(other, join='left', overwrite=True, filter_func=None, errors='ignore')[source]
#     - Modify **in place using non-NA values** from another DataFrame.
#     - **Aligns on indices.** There is no return value.
#
# - Parameters :
#     - other DataFrame, or object coercible into a DataFrame
#         - Should have **at least one matching index/column label with the original DataFrame**. If a Series is passed, its name attribute must be set, and that will be used as the column name to align with the original DataFrame.
#   
#     - join{‘left’}, default ‘left’
#         - **Only left join is implemented, keeping the index and columns of the original object.**
#
#     - overwrite bool, default True
#         - How to handle non-NA values for overlapping keys:
#         - **True: overwrite original DataFrame’s values with values from other.**
#         - **False: only update values that are NA in the original DataFrame.**
#
#     - filter_func callable(1d-array) -> bool 1d-array, optional
#         - Can choose to replace values other than NA. Return True for values that should be updated.
#  
#     - errors {‘raise’, ‘ignore’}, default ‘ignore’
#         - If ‘raise’, will raise a ValueError if the DataFrame and other both contain non-NA data in the same place.
#         - Changed in version 0.24.0: Changed from raise_conflict=False|True to errors=’ignore’|’raise’.
#
# - Returns : None method directly changes calling object
# - Raises : ValueError
#     - When errors=’raise’ and there’s overlapping non-NA data.
#     - When errors is not either ‘ignore’ or ‘raise’
#     - NotImplementedError : If join != ‘left’

df = pd.DataFrame({'A': ['a', 'b', 'c'],
                   'B': ['x', 'y', 'z']})
df
new_df = pd.DataFrame({'B': ['d', 'e']}, index=[1, 2])
new_df
df.update(new_df)
df

# ### overwrite (bool) : default True : Defines How to handle non-NA values for overlapping keys :
# - **False: only update values that are NA in the original DataFrame.**

# +
df = pd.DataFrame({'A': ['a', 'b', 'c'],
                   'B': ['x', 'y', 'z']})
df
new_df = pd.DataFrame({'B': ['d', 'e']}, index=[1, 2])
new_df
df.update(new_df, overwrite=False)
df

# Here the values in the overlpping indexes of original dataframe IS NOT updated.
# With the option overwrite=false, it only updates when the original dataframe has NaNs in overlapping indexes.

# +
df = pd.DataFrame({'A': ['a', 'b', 'c'],
                   'B': ['x', np.NaN, 'z']})
df
new_df = pd.DataFrame({'B': ['d', 'e']}, index=[1, 2])
new_df
df.update(new_df, overwrite=False)
df

# Here the values in the overlpping indexes of original dataframe IS Updated.
# With the option overwrite=false, it only updates when the original dataframe has NaNs in overlapping indexes.
# -

# ### If other contains NaNs the corresponding values are not updated in the original dataframe.

df = pd.DataFrame({'A': ['a', 'b', 'c'],
                   'B': ['x','y', 'z']})
df
new_df = pd.DataFrame({'B': ['d', np.NaN]}, index=[1, 2])
new_df
df.update(new_df)
df

# ## ```take```
# - ```DataFrame.take(indices, axis=0, is_copy=None, ****kwargs)```[source]
#     - Return the elements in the given positional indices along an axis.
#
#     - This means that we are not indexing according to actual values in the index attribute of the object. We are indexing according to the actual position of the element in the object.
#
# - Parameters :
#     - indices array-like : An array of ints indicating which positions to take.
#     - axis {0 or ‘index’, 1 or ‘columns’, None}, default 0
#         - The axis on which to select elements. 0 means that we are selecting rows, 1 means that we are selecting columns.
#         
# - **https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.take.html**

df = pd.DataFrame([('falcon', 'bird', 389.0),
                   ('parrot', 'bird', 24.0),
                   ('lion', 'mammal', 80.5),
                   ('monkey', 'mammal', np.nan)],
                  columns=['name', 'class', 'max_speed'],
                  index=[0, 2, 3, 1])
df


# +
# the actual indices selected (0 and 1) do not correspond to our selected indices 0 and 3

df.take([0, 3])
# -

# _Take elements at indices 1 and 2 along the axis 1 (column selection)._

df.take([1, 2], axis=1)

#  _Take elements using negative integers for positive indices, starting from the end of the object, just like with Python lists._

df.take([-1, -2])

# ### Showing the behaviour of ```.iloc()``` and ```.loc()```

df

df.iloc[[0,3]]

df.loc[[0,3]]

df.iloc[df.index[[0,3]]]
df.index
df.index[[0,3]]

# ## ```truncate()```

# ```DataFrame.truncate(before=None, after=None, axis=None, copy=True)```[source]
# - Truncate a Series or DataFrame **before and after some index value.**
#
#     - This is a useful shorthand for boolean indexing based on index values above or below certain thresholds.
#
# - Parameters : 
#     - before - date, str, int : Truncate all rows before this index value.
#
#     - after - date, str, int : Truncate all rows after this index value.
#
#     - axis - {0 or ‘index’, 1 or ‘columns’}, optional : Axis to truncate. Truncates the index (rows) by default.
#
#     - copy - bool, default is True, Return a copy of the truncated section.
#
# - Returns : type of caller : The truncated Series or DataFrame.

df2 = df.copy()
df2

# +
# df2.truncate(before=2, after =3)

# Truncate requires a sorted index
# -

# ![image.png](attachment:image.png)

# +
# So we will sort the dataframe based on index

# By default, axis= 0  / 'rows'
df2.sort_index(axis= 'rows', inplace=True)
df2
# -

df2.truncate(before=2, after =3)


