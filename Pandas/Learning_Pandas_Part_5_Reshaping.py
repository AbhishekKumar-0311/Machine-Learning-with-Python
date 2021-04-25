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

# +
# To get multiple outputs in the same cell

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# +
# Import the required libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
# -

# # Wide to Long DataFrame
# One record to many records based on a ID column
#
# ```py
# 1. df.melt(id_vars=[ ], value_vars=[ ], var_name=[ ], value_name=[ ])
# 2. pd.wide_to_long(df, i=[ ], j=[ ], stubnames=[ ], sep="_") 
# # stubnames provides the flexibility to add the multiple sets of series of variables```
#     apply reset_index() to flatten out the indices and make the it more usable.
#

# ## df.melt()

df = pd.DataFrame({'id': [1,2],
                   'name': ['a','b'],
                   'prem1' : [100,280],
                   'prem2' : [200,180],
                   'prem3' : [300,80],})
df

df_melted = df.melt(id_vars=['id','name']).sort_values('id')
df_melted

df2 = pd.DataFrame({'id': [1,2],
                   'name': ['a','b'],
                   'prem1' : [100,280],
                   'prem2' : [np.NaN,180],
                   'prem3' : [300,np.NaN],})
df2

df2_melted = df2.melt(id_vars=['id','name'], var_name = 'month', value_name = 'premiums').sort_values('id')
df2_melted

# +
# df2_melted = df2_melted.loc[]

# +
df3 = df2.copy()

df3_melted = df3.melt(id_vars=['id'], value_vars=['prem1','prem2','prem3'], var_name = 'month', value_name = 'premiums').sort_values('id')
df3_melted
# -

# ### Example 2

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

# +
# Sample data set-up

emp_df_1 = emp_df.copy()

emp_df_1['Holi_Bonus'] = emp_df_1['Salary']*0.05
emp_df_1['Diwali_Bonus'] = emp_df_1['Salary']*0.075
emp_df_1['Yearly_Bonus'] = emp_df_1['Salary']*0.10
emp_df_1
# -

emp_df_1_long = emp_df_1.melt(id_vars = ['Emp_Id','Emp_Name'] , 
                              value_vars = [ 'Holi_Bonus','Diwali_Bonus','Yearly_Bonus' ],
                              var_name = 'Event',
                              value_name = 'Bonus' )
emp_df_1_long

# ## pd.wide_to_long()

df4 = pd.DataFrame({'id': [1,2],
                   'name': ['a','b'],
                   'prem1' : [100,280],
                   'prem2' : [np.NaN,180],
                   'prem3' : [300,np.NaN],
                   'disc1' : [20,40],
                   'disc2' : [np.NaN,30],
                   'disc3' : [50,np.NaN],})
df4

# +
# melt is not working as expected.
# There are 2 sets of sequential columns and both the sets are transposed to the same column
# NOT Working as EXPECTED

# df4_melted = df4.melt(id_vars=['id','name'], value_vars=['prem1','prem2','prem3','disc1','disc2','disc3'], var_name = 'month', value_name = 'values').sort_values('id').reset_index(drop='index')
# df4_melted
# -

# #### Another way to transform is to use the wide_to_long() panel data convenience function. It is less flexible than melt(), but more user-friendly.

df4_melted1 = pd.wide_to_long(df4, i=['id','name'], j='month', stubnames=['prem','disc'])
df4_melted1

df4_melted1.reset_index(inplace=True)
df4_melted1

# +
# Trying to see the usage of suffix= parameter. Not completed yet.
# df4_melted2 = pd.wide_to_long(df4, i=['id','name'], j='month', stubnames=['prem','disc'])#, suffix='1')
# df4_melted2
# -

# ## df.stack()

df5 = pd.DataFrame({'id': [1,2],
                   'name': ['a','b'],
                   'prem1' : [100,280],
                   'prem2' : [np.NaN,180],
                   'prem3' : [300,np.NaN]})
df5

df5.set_index(['id','name']).stack().reset_index()

#     > 1. Important thing to note - there is single series of variable (perm1 - perm3), which is transposed here.
#     > 2. The index is set before the process of stacking.
#     > 3. If there is multile sets of series of variables, then this would not work as expected.
#     > 4. By default, dropna = True, and hence it drops the NaN values

df5.set_index(['id','name']).stack(dropna=False).reset_index()

df6 = pd.DataFrame({'id': [1,2],
                   'name': ['a','b'],
                   'prem1' : [100,280],
                   'prem2' : [np.NaN,180],
                   'prem3' : [300,np.NaN],
                   'disc1' : [20,40],
                   'disc2' : [np.NaN,30],
                   'disc3' : [50,np.NaN]})
df6

df6_stacked = df6.set_index(['id','name']).stack().reset_index()
df6_stacked

# +
# stack is not working as expected.
# There are 2 sets of sequential columns and both the sets are transposed to the same column
# NOT Working as EXPECTED
# -



# # Long to Wide DataFrame
# Multiple records per ID to a single(one) record of each ID.
#
# ```python
# 1. pd.pivot()
# 2. pd.pivot_table()
# 3. Use df.set_index([id_vars columns and var_name columns]) and chain it with .unstack(level=2 (here))```

# ### pd.pivot() - Does not work for multiple indexes, So in this case, does not work

# ### pd.pivot_table() - Although it is for aggregation, it worked to change LONG to WIDE Data

df4_melted1

df_wide = pd.pivot_table(df4_melted1, index=['id','name'], columns='month', values=['prem','disc'])
df_wide

df_wide.columns

# +
# df_wide = df4_melted1.pivot(index=['id','name'], columns='month', values=['prem'])
# df_wide
# -

df_wide.columns = ['_'.join(map(str, tup)) for tup in df_wide.columns]
df_wide.reset_index()

# ### df.unstack() - 
# #### Use df.set_index([id_vars columns and var_name columns]) and chain it with .unstack(level=2 (here))

wide_df = df4_melted1.set_index(['id','name','month']).unstack(level=2)
wide_df

# ID: level = 0; RegionVariable: level = 1; 'EXP': level = 2; 'ModelID': level = 3;

wide_df.columns

# +
# Code to flatten the list and at the same time concatenating it.

wide_df.columns = ['_'.join(map(str, tup)) for tup in wide_df.columns] # Everything is back to the first dataframe
# -

wide_df.columns

wide_df

wide_df.reset_index()



# ### Example 2

emp_df_1_long

emp_df_1_wide_1 = emp_df_1_long.pivot_table(index =  ['Emp_Id','Emp_Name'] ,
                                          columns = 'Event',
                                          values = 'Bonus' ).reset_index()
emp_df_1_wide_1

emp_df_1_wide_2 = emp_df_1_long.pivot_table(index =  ['Emp_Id','Emp_Name'] ,
                                           columns = 'Event',
                                           values = 'Bonus',
                                           margins = True ).reset_index()  # default aggfunc = 'mean'
emp_df_1_wide_2

emp_df_1_wide_3 = emp_df_1_long.pivot_table(index =  ['Emp_Id','Emp_Name'] ,
                                           columns = 'Event',
                                           values = 'Bonus',
                                           margins = True,
                                           aggfunc = 'sum').reset_index()
emp_df_1_wide_3

# +
# Only row-wise aggregation

emp_df_1_wide_4 = emp_df_1_long.pivot_table(index =  ['Emp_Id','Emp_Name']) # default aggfunc = 'mean'
emp_df_1_wide_4
# -

emp_df_1_wide_4 = emp_df_1_long.pivot_table(index =  ['Emp_Id','Emp_Name'] ,
                                           columns = 'Event',
                                           values = 'Bonus',
                                           fill_value = 1000)
emp_df_1_wide_4

# ### There are other techniques that enables Re-Shaping of dataframes.
#
#     i. pivot()
#     ii. stack() & unstack()
#     iii. wide_to_long()
#     iv. crosstab()
#     v. cut()


