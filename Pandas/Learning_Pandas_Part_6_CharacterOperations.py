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

# ## 1. Dataframe creation

# +
salary = [['Google', 'Machine Learning Engineer', 121000],
['Google', 'Data Scientist', 109000],
['Google', 'Tech Lead', 129000],
['Facebook', 'Data Scientist', 103000]]

columns_name=['Company', 'Job','Salary']

emp_df = pd.DataFrame(salary,columns=columns_name)
emp_df
# -

#
#
# - https://www.listendata.com/2019/06/python-string-functions.html

# ### List of frequently used string functions

# |Function	    							|Description																		|MS EXCEL FUNCTION |
# |:-|:-|:-|
# |len( )										|Calculate length of string															|LEN( )            |
# |mystring[:N]								|Extract N number of characters from start of string.								|LEFT( )           |
# |mystring[-N:]								|Extract N number of characters from end of string									|RIGHT( )          |
# |mystring[X:Y]								|Extract characters from middle of string, starting from X position and ends with Y	|MID( )            |
# |str.split()								|Split each string with the given pattern.											|-                 |
# |str.replace(old_substring, new_substring)	|Replace a part of text with different sub-string									|REPLACE( )        |
# |str.contains('pattern', case=False)		|Returns a Boolean value True for each element if the substring contains in the element, else False	|SQL LIKE Operator |
# |str.extract(regular_expression)			|Return matched values (Pandas Function)											|-                 |
# |str.count('sub_string')					|Count occurence of pattern in string												|-                 |
# |cat(sep=' ')								|Concatenates the series/index elements with given separator.						|-                 |
# |separator.join(str)						|Concatenate Strings																|CONCATENATE( )    |
# |strip(),lstrip(),rstrip()					|Helps strip whitespace(including newline) from each string in the Series/index from both the sides.|  |
# |repeat(value)								|Repeats each element with specified number of times.								|-                 |
# |startswith(pattern)						|Returns true if the element in the Series/Index starts with the pattern.			|-                 |
# |endswith(pattern)  						|Returns true if the element in the Series/Index ends with the pattern.				|-                 |
# |find(pattern)								|Returns the first position of the first occurrence of the pattern.					|-                 |
# |findall(pattern)							|Returns a list of all occurrence of the pattern.									|-                 |
# |str.lower()								|Convert characters to lowercase													|LOWER( )          |
# |str.upper()								|Convert characters to uppercase													|UPPER( )          |
# |str.swapcase()								|Swaps the case lower/upper.  														|-                 |
# |str.isalnum()								|Check whether string consists of only alphanumeric characters						|-                 |
# |str.islower()								|Check whether characters are all lower case										|-                 |
# |str.isupper()								|Check whether characters are all upper case										|-                 |
# |str.isnumeric()							|Check whether string consists of only numeric characters							|-                 |
# |str.isspace()								|Check whether string consists of only whitespace characters						|-                 |
#
#

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

# Setup Data
df = df_sample.copy()
df

# ## SPLIT()
# - SCAN in SAS

df['City'] = df['col_a'].str.split(',').str[0]
df
df['State'] = df['col_a'].str.split(',').str[1]
df

# ## REPLACE()
# - TRANWRD in SAS

df['NewColA'] = df['col_a'].str.replace('TX', 'Abhishek')
df

# +
# Replacing 1st word of col_a with Mumbai

# df['NewColA'] = df['col_a'].str.replace(df['col_a'].str.split(',').str[0], 'Mumbai')
# df
# -

# ## CAT()
# - catx, cats in SAS

df['Location1'] = df['City'] + '-' + df['State']
df

df['Location2'] = df['City'].str.strip().str.cat(df['State'].str.strip(), sep= ':::')
df

# ## Slicing using Index
# - SUBSTR in SAS

df['substring1'] = df['Location2'].str[-2:]
df

df['substring2'] = df['Location2'].str[0:3]
df

df['substring3'] = df['Location2'].str[2::-1]
df

# ## STRIP( ' ' )
# - strip(), lstrip(), rstrip()
# - Stripping is like trimming tree branches. We can remove spaces or any other characters at the beginning or end of a string. like, strip('$') - remove dollar sign from both left and right side
#
# - STRIP, TRIM in SAS

df['NewColB'] = df['col_b'].str.strip('K')
df



















# +
# df1 = df
# df1

# +
# df == df1
# -


