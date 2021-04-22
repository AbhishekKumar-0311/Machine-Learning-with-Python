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
          ['5','Anusha Yenduri','AIML', 'Data Scientist','F', 'Y', '01011989',  921000],
          ['6','Ritesh Srivastava','AIML', 'Data Engineer','M', 'Y', np.NaN, 785000]]

columns_name=['Emp_Id','Emp_Name','Department','Role','Gender', 'WFH Status', 'DOB', 'Salary']

emp_df = pd.DataFrame(salary,columns=columns_name)
emp_df
# -

# # 1. Reshaping with Melt
#
# There are many different ways to reshape a pandas dataframe from wide to long form.
# But the melt() method is the most flexible

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



# # 2. Reshaping with Pivot_table
#
# The pivot_table() method is the most flexible to reshape pandas dataframes from long to wide in Python

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





















































# ### References:
#
# #### 1. [Pandas Documentation](#https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html)
# #### 2. [TDS](#https://towardsdatascience.com/reshape-pandas-dataframe-with-melt-in-python-tutorial-and-visualization-29ec1450bb02)
