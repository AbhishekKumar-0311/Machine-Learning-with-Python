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

# ## List of frequently used string functions

# |Function	    							|Description																		|MS EXCEL FUNCTION |
# |:-|:-|:-|
# |len( )										|Calculate length of string															|LEN( )            |
# |mystring[:N]								|Extract N number of characters from start of string.								|LEFT( )           |
# |mystring[-N:]								|Extract N number of characters from end of string									|RIGHT( )          |
# |mystring[X:Y]								|Extract characters from middle of string, starting from X position and ends with Y	|MID( )            |
# |str.split(),rsplit()						|Split each string with the given pattern.											|-                 |
# |cat(sep=' ')								|Concatenates the series/index elements with given separator.						|-                 |
# |separator.join(str)						|Concatenate Strings																|CONCATENATE( )    |
# |str.replace(old_substring, new_substring)	|Replace a part of text with different sub-string									|REPLACE( )        |
# |str.count('sub_string')					|Count occurence of pattern in string												|-                 |
# |strip(),lstrip(),rstrip()					|Helps strip whitespace(including newline) from each string in the Series/index from both the sides.|  |
# |repeat(value)								|Repeats each element with specified number of times.								|-                 |
# |startswith(pattern)						|Returns true if the element in the Series/Index starts with the pattern.			|-                 |
# |endswith(pattern)  						|Returns true if the element in the Series/Index ends with the pattern.				|-                 |
# |str.contains('pattern', case=False)		|Returns a Boolean value True for each element if the substring contains in the element, else False	|SQL LIKE Operator |
# |match(pattern)								|Determine if each string starts with a match of a regular expression.				|-                 |
# |fullmatch(pattern)							|Stricter matching that requires the entire string to match.						|-                 |
# |index(pattern),rindex()					|Return lowest indexes in each string in Series/Index.								|-                 |
# |find(pattern),rfind()						|Returns the first position of the first occurrence of the pattern.					|-                 |
# |findall(pattern)							|Returns a list of all occurrence of the pattern.									|-                 |
# |str.extract(regular_expression)			|Return matched values (Pandas Function)											|-                 |
# |str.extractall(regular_expression)			|Return matched values (Pandas Function)											|-                 |
# |str.zfill(n)								|Pad strings in the Series/Index by prepending ‘0’ characters.						|-                 |
# |str.ljust(width, fillchar=' ')				|Fills the right side of strings with an arbitrary character. 						|-                 |
# |str.rjust(width, fillchar=' ')				|Fills the left side of strings with an arbitrary character.						|-                 |
# |str.center(width, fillchar=' ')			|Fills both sides of strings with an arbitrary character.							|-                 |
# |str.pad(width,side='left',fillchar='%')	|Pad strings in the Series/Index up to width.										|-                 |
# |str.lower()								|Convert characters to lowercase													|LOWER( )          |
# |str.upper()								|Convert characters to uppercase													|UPPER( )          |
# |str.swapcase()								|Swaps the case lower/upper.  														|-                 |
# |str.title()								|Converts first character of each word to uppercase and remaining to lowercase.		|-                 |
# |str.capitalize()							|Converts first character to uppercase and remaining to lowercase.					|-                 |
# |str.isalnum()								|Check whether string consists of only alphanumeric characters						|-                 |
# |str.isdigit()								|Check whether string consists of only digit characters								|-                 |
# |str.isalpha()								|Check whether string consists of only alphabets characters							|-                 |
# |str.isdecimal()							|Check whether string consists of only decimals characters							|-                 |
# |str.isnumeric()							|Check whether string consists of only numeric characters							|-                 |
# |str.isspace()								|Check whether string consists of only whitespace characters						|-                 |
# |str.islower()								|Check whether characters are all lower case										|-                 |
# |str.isupper()								|Check whether characters are all upper case										|-                 |
# |str.istitle()								|Check whether characters are all title case										|-                 |

#
#
# - https://www.listendata.com/2019/06/python-string-functions.html

# ## 1. Dataframe creation

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



# ## LEN()
# - LENGTH() in SAS

# +
# Setup Data
df1 = df.copy()
df1

df1['LenOfColA'], df1['LenOfColB'] = df1['col_a'].str.len() ,  df1['col_b'].str.len()
df1
# -

# ## Slicing using Index
# - SUBSTR in SAS

# +
# Setup Data
df2 = df.copy()
df2

df2['substring1'] = df2['col_a'].str[-2:]
df2
# -

df2['substring2'] = df2['col_a'].str[0:3]
df2

df2['substring3'] = df2['col_a'].str[2::-1]
df2

# ## SPLIT()
# - SCAN in SAS
# - .str.split(pat=None, n=- 1, expand=False)[source]
# - Parameters
#     - pat - string or regex to split on
#     - n - number of splits
#     - expand - True/False : If True, return DataFrame/MultiIndex expanding dimensionality.
# - https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html
# - https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rsplit.html

# +
# Setup Data
df3 = df.copy()
df3

df3['City'] = df3['col_a'].str.split(',').str[0]
df3
df3['State'] = df3['col_a'].str.split(',').str[1]
df3
df3['State2'] = df3['col_a'].str.split(',').str.get(1)
df3
# -

# ### Between different symbols
# - The goal is to obtain the digits between two different symbols (the dash symbol and the dollar symbol)
#     - First, set the variable (i.e., betweenTwoDifferentSymbols) to obtain all the characters after the dash symbol
#     - Then, set the same variable to obtain all the characters before the dollar symbol

# +
Data = {'Identifier': ['IDAA-111$AA','IDB-2222222$B','IDCCC-33$CCC']}
dfi = pd.DataFrame(Data, columns= ['Identifier'])

Data
dfi

betweenTwoDifferentSymbols = dfi['Identifier'].str.split('-').str[1]
dfi['betweenTwoDifferentSymbols'] = betweenTwoDifferentSymbols.str.split('$').str[0]

dfi
# -

# ## CAT()
# - catx, cats in SAS
# - sep = ' , '
# - na_rep = '?' - It replaces the NaN with question-mark ( ? )

# ### Concat 2 columns
# - In the same way, it could be extended for more columns
#     - ```df['combined']=df['bar']+'_'+df['foo']+'_'+df['new']```

# +
# Setup Data
df4 = df3.copy()
df4

df4['Location1'] = df4['City'] + '-' + df4['State']
df4
# -

# ### Concat 2 columns using series.str.cat()
# - sep = ' , ' - To add separator in between columns
# - na_rep = '?' - It replaces the NaN with question-mark ( ? )
# - https://pandas.pydata.org/docs/reference/api/pandas.Series.str.cat.html

df4['Location2'] = df4['City'].str.strip().str.cat(df4['State'].str.strip(), sep= ':::')
df4

# ### Concat 2 or more columns
# - 2 or more columns can be added by providing list of values as shown below

df4['Cat3'] = df4['City'].str.strip().str.cat([df4['State'],df4['col_c']], sep= ':::')
df4

# ### Technique to perform concat on non-string columns
# - ```df['combined']=df['bar'].astype(str)+'_'+df['foo']+'_'+df['new']```
# - ```df['Full Date'] = df['Day'].map(str) + '-' + df['Month'].map(str) + '-' + df['Year'].map(str)```

# ## STR.JOIN()

# Setup Data
df5 = df3.copy()
df5



# ## REPLACE()
# - TRANWRD in SAS
# - str.replace(old_text,new_text,case=False) is used to replace a particular character(s) or pattern with some new value or pattern.
# - .str.replace(pat, repl, n=- 1, case=None, flags=0, regex=None)[source]
# - https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html

# +
# Setup Data
df6 = df.copy()
df6

df6['NewColA1'] = df6['col_a'].str.replace('TX', 'Abhishek')
df6
df6['NewColA2'] = df6['col_a'].str.replace('tX', ' ', case= False)
df6
df6['LenNewColA2'] = df6['NewColA2'].str.len()
df6

# +
# Replacing 1st word of col_a with Mumbai

# df['NewColA'] = df['col_a'].str.replace(df['col_a'].str.split(',').str[0], 'Mumbai')
# df
# -

# ## COUNT( )
# - It returns the count of the appearance of pattern in each element in Data-Frame like below in example it counts ‘n’ in each string of DataFrame and returns the total counts of ‘n’ in each string.
# - In SAS
#     - COUNT  : Count characters
#     - COUNTW : Count words in SAS
#     - COUNTC : Count specific character in SAS

# +
# Setup Data
df7 = df.copy()
df7

import re
df7['CountA'] = df7['col_a'].str.count('c',re.I)
df7
# -

# ### Count No. of Words

df7['NoOfWords1'] = [len(x.split(',')) for x in df7['col_a'].tolist()]
df7

df7['NoOfWords2'] = df7['col_a'].str.split(',').str.len()
df7
df7['NoOfWords3'] = df7['col_a'].str.split(',').apply(len)
df7

import re
df7['NoOfWords4'] = df7['col_a'].str.count('\w+')
df7

import re
df7['NoOfWords5'] = df7['col_a'].str.count('^[cpiad]\w+', re.I)
df7

# ## STRIP( ' ' )
# - strip(), lstrip(), rstrip()
# - Stripping is like trimming tree branches. We can remove spaces or any other characters at the beginning or end of a string. like, strip('$') - remove dollar sign from both left and right side
#
# - STRIP, TRIM in SAS

# +
# Setup Data
df8 = df.copy()
df8

df8['NewColB'] = df8['col_b'].str.strip('K')
df8
# -

# ## REPEAT()
# - REPEAT() in SAS

# +
# Setup Data
df9 = df.copy()
df9

df9['RepeatColD'] = df9['col_d'].str.repeat(3)
df9
# -

# ## STARTSWITH()
# - .str.startswith(pat, na=None)
# - na = False : Specifying na to be False instead of NaN.
# - Using SUBSTR() in SAS
# - https://pandas.pydata.org/docs/reference/api/pandas.Series.str.startswith.html

# +
# Setup Data
df10 = df.copy()
df10

df10[df10.col_a.str.startswith('C')]
# -

# ### It's possible to pass a tuple of prefixes to startswith() method in Python.
# - If the string starts with any item of the tuple, startswith() returns True. If not, it returns False

df10[df10.col_a.str.startswith(('C','P'))]

# ## ENDSWITH()
# - .str.endswith(pat, na=None)[source]
# - na = False : Specifying na to be False instead of NaN.
# - Using SUBSTR() in SAS
# - https://pandas.pydata.org/docs/reference/api/pandas.Series.str.endswith.html

# +
# Setup Data
df11 = df.copy()
df11

df11[df11.col_a.str.endswith('X')]
# -

# ## CONTAINS()
# - Using CONTAINS() in SAS
# - .str.contains(pat, case=True, flags=0, na=None, regex=True)[source]
# - Test if pattern or regex is contained within a string of a Series or Index.
# - Return boolean Series or Index based on whether a given pattern or regex is contained within a string of a Series or Index.
# - Parameters
#     - pat : str :  Character sequence or  **regular expression**.
#     - case : bool : default True If True, case sensitive.
#     - flags : int : default 0 (no flags) Flags to pass through to the re module, e.g. re.IGNORECASE.
#     - na : scalar : optional Fill value for missing values, eg False . The default depends on dtype of the array. For object-dtype, numpy.nan is used. For StringDtype, pandas.NA is used.
#     - regex : bool : default True If True, assumes the pat is a regular expression.
#         - If False, treats the pat as a literal string.

# Setup Data
df12 = df.copy()
df12

bool = df12.col_a.str.contains('oU', flags = re.IGNORECASE)
df12[bool]

bool = df12.col_a.str.contains(('tx|ca'), case = False)
df12[bool]

bool = df12.col_b.str.contains(('^[0-6].*'), case = False)
df12[bool]

bool = df12.col_a.str.contains('z', flags = re.IGNORECASE)
df12[bool]

# +
# Ending with TX , ignore case

bool = df12.col_a.str.contains('tx$', flags = re.IGNORECASE, regex=True)
df12[bool]

# +
# Ending with 2 characters , ignore case

bool = df12.col_a.str.contains('\w{2}$', flags = re.IGNORECASE, regex=True)
df12[bool]
# -

# ## str.MATCH
# - str.match(pat, case=True, flags=0, na=None)[source]
# - Determine if each string starts with a match of a regular expression.
# - Parameters
#     - pat : Character sequence or **regular expression**.
#     - case : bool : True, if case sensitive
#     - flags : Regex module flags, e.g. re.IGNORECASE.
#     - na : Fill value for missing values.
# - Returns : Series/array of boolean values

# Setup Data
df13 = df.copy()
df13

bool = df13.col_a.str.match('h', flags = re.IGNORECASE)
df13[bool]

bool = df13.col_a.str.match('h', case = False)
df13[bool]

bool = df13.col_b.str.match('62.*k', case = False)
df13[bool]

# ## str.FULLMATCH
# - str.fullmatch(pat, case=True, flags=0, na=None)[source]
# - Determine if each string starts with a match of a regular expression.
# - Parameters
#     - pat : Character sequence or **regular expression**.
#     - case : bool : True, if case sensitive
#     - flags : Regex module flags, e.g. re.IGNORECASE.
#     - na : Fill value for missing values.
# - Returns : Series/array of boolean values

bool = df13.col_b.str.fullmatch('62.*')
df13[bool]

bool = df13.col_b.str.fullmatch('62K-70k', case= False)
df13[bool]

# ## str.INDEX
# - Series.str.index(sub, start=0, end=None)[source]
# - Return lowest indexes in each string in Series/Index.
# - Returns ValueError on failure, when the substring is not found.
# - Parameters
#     - sub - substring being searched
#     - start - int, left edge index
#     - end - int, right edge index

# Setup Data
df14 = df.copy()
df14

# +
# Its not working as expected

# bool = df14.col_a.str.index('Dallas',start=0)
# df14[bool]
# -

# ## str.FIND
# - Series.str.find(sub, start=0, end=None)[source]
# - Return lowest indexes in each string in Series/Index.
# - Return -1 on failure, unlike INDEX(), which returns ValueError
# - Parameters
#     - sub - substring being searched
#     - start - int, left edge index
#     - end - int, right edge index
#     
# - RFIND() - Return highest indexes in each strings in the Series/Index.

# Setup Data
df15 = df.copy()
df15

df15['isA'] = df15.col_a.str.find('Dallas',start=0, end=6)
df15

df15['isA1'] = df15.col_a.str.find('TX')
df15

df15['isA2'] = df15.col_a.str.rfind('San')
df15

# ## str.FINDALL
# - Series.str.findall(pat, flags=0)[source]
# - Find all occurrences of pattern or regular expression in the Series/Index.
# - Equivalent to applying re.findall() to all the elements in the Series/Index.
# - Parameters
#     - pat - Pattern or **regular expression**.
#     - flags - Flags from re module, e.g. re.IGNORECASE (default is 0, which means no flags).
# - Return - All non-overlapping matches of pattern or regular expression in each string of this Series/Index.

# Setup Data
df16 = df.copy()
df16

# ### If the pattern is found more than once in the same string, then a list of multiple strings is returned:

matches = df16['col_a'].str.repeat(3).str.findall('Go', flags=re.I)
type(matches)
matches
matches[2][2]

matches = df16['col_a'].str.repeat(3).str.findall('go', flags=re.I)
type(matches)
matches
matches[:][2]

# ## str.extract
# Series.str.extract(pat, flags=0, expand=True)[source]
# - Extract capture groups in the regex pat as columns in a DataFrame.
#
# - For each subject string in the Series, extract groups from the first match of regular expression pat.
#
# - Parameters
#     - patstr - Regular expression pattern with capturing groups.
#  
#     - flagsint, default 0 (no flags) - Flags from the re module, e.g. re.IGNORECASE, that modify regular expression matching for things like case, spaces, etc. For more details, see re.
#
#     - expandbool, default True - If True, return DataFrame with one column per capture group. If False, return a Series/Index if there is one capture group or DataFrame if there are multiple capture groups.
#
# - Returns - DataFrame or Series or Index
#     - A DataFrame with one row for each subject string, and one column for each group. Any capture group names in regular expression pat will be used for column names; otherwise capture group numbers will be used. The dtype of each result column is always object, even when no match is found. If expand=False and pat has only one capture group, then return a Series (if subject is a Series) or Index (if subject is an Index).
#     
# - https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html



# ## str.extractall
# - Series.str.extractall(pat, flags=0)[source]
# - Extract capture groups in the regex pat as columns in DataFrame.
# - For each subject string in the Series, extract groups from all matches of regular expression pat. When each subject string in the Series has exactly one match, extractall(pat).xs(0, level=’match’) is the same as extract(pat).
# - Parameters
#     - patstr - Regular expression pattern with capturing groups.
#     - flagsint, default 0 (no flags)
#     - A re module flag, for example re.IGNORECASE. These allow to modify regular expression matching for things like case, spaces, etc. Multiple flags can be combined with the bitwise OR operator, for example re.IGNORECASE | re.MULTILINE.
# - Returns - DataFrame
#     - A DataFrame with one row for each match, and one column for each group. Its rows have a MultiIndex with first levels that come from the subject Series. The last level is named ‘match’ and indexes the matches in each item of the Series. Any capture group names in regular expression pat will be used for column names; otherwise capture group numbers will be used.
#     
# - https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extractall.html#pandas.Series.str.extractall



# ## https://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html

# |Function	    							|Description																		|MS EXCEL FUNCTION |
# |:-|:-|:-|
# |str.zfill(n)								|Pad strings in the Series/Index by prepending ‘0’ characters.						|-                 |
# |str.ljust(width, fillchar=' ')				|Fills the right side of strings with an arbitrary character. 						|-                 |
# |str.rjust(width, fillchar=' ')				|Fills the left side of strings with an arbitrary character.						|-                 |
# |str.center(width, fillchar=' ')			|Fills both sides of strings with an arbitrary character.							|-                 |
# |str.pad(width,side='left',fillchar='%')	|Pad strings in the Series/Index up to width.										|-                 |

# ### str.zfill(width)[source]
# - width - Minimum length of resulting string

# ### str.rjust(width, fillchar=' ')[source]
# - Pad left side of strings in the Series/Index.
# - width - Minimum width of resulting string
# - fillchar - Additional character for filling, default is whitespace.

# ### str.ljust(width, fillchar=' ')[source]
# - Pad right side of strings in the Series/Index.
# - width - Minimum width of resulting string
# - fillchar - Additional character for filling, default is whitespace.

# ### str.center(width, fillchar=' ')[source]
# - Pad left and right side of strings in the Series/Index.
# - width - Minimum width of resulting string
# - fillchar - Additional character for filling, default is whitespace.

# ### .str.pad(width, side='left', fillchar=' ')[source]
# - Pad strings in the Series/Index up to width.
# - Parameters
#     - width - int, minimum width of resulting string
#     - side - left, right, both - Side from which to fill resulting string.
#     - fillchar - Additional character for filling, default is whitespace.
# - Series.str.pad(side='left') : Series.str.rjust
# - Series.str.pad(side='right') : Series.str.ljust
# - Series.str.pad(side='both') : Series.str.center
# - Series.str.pad(side='left', fillchar='0') : Series.str.zfill



# ## https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html

# |Function	    							|Description																		|MS EXCEL FUNCTION |
# |:-|:-|:-|
# |str.lower()								|Convert characters to lowercase													|LOWER( )          |
# |str.upper()								|Convert characters to uppercase													|UPPER( )          |
# |str.swapcase()								|Swaps the case lower/upper.  														|-                 |
# |str.title()								|Converts first character of each word to uppercase and remaining to lowercase.		|-                 |
# |str.capitalize()							|Converts first character to uppercase and remaining to lowercase.					|-                 |



# ## https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isalpha.html

# |Function	    							|Description																		|MS EXCEL FUNCTION |
# |:-|:-|:-|
# |str.isalnum()								|Check whether string consists of only alphanumeric characters						|-                 |
# |str.isdigit()								|Check whether string consists of only digit characters								|-                 |
# |str.isalpha()								|Check whether string consists of only alphabets characters							|-                 |
# |str.isdecimal()							|Check whether string consists of only decimals characters							|-                 |
# |str.isnumeric()							|Check whether string consists of only numeric characters							|-                 |
# |str.isspace()								|Check whether string consists of only whitespace characters						|-                 |
# |str.islower()								|Check whether characters are all lower case										|-                 |
# |str.isupper()								|Check whether characters are all upper case										|-                 |
# |str.istitle()								|Check whether characters are all title case										|-                 |



# # Object vs String
# Before pandas 1.0, only “object” datatype was used to store strings which cause some drawbacks because non-string data can also be stored using “object” datatype. Pandas 1.0 introduces a new datatype specific to string data which is StringDtype. As of now, we can still use object or StringDtype to store strings but in the future, we may be required to only use StringDtype.
# One important thing to note here is that object datatype is still the default datatype for strings. To use StringDtype, we need to explicitly state it.
# We can pass “string” or pd.StringDtype() argument to dtype parameter to string datatype.
#
# ![image.png](attachment:image.png)










# ## Problem Solving

# +
# Replacing 2nd word of col_a with 1st word of col_a

dfp = df.copy()
dfp

dfp['DupA'] = dfp['col_a']
dfp

x = dfp.col_a.str.split(',').str[0]

def func(row):
    return row['DupA'].replace(row['DupA'].split(',')[1], row['DupA'].split(',')[0])


dfp['DupA'] = dfp.apply(func, axis = 1)

dfp

d2= dfp.apply(func, axis = 1)

d2
# -
features['sl_mm2'] = features['sepal length (cm)'].apply(lambda x : x*10)
features.head()


