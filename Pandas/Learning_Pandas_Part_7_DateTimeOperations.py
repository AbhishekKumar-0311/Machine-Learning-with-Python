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

# ### WarmUp

date = pd.to_datetime('12Apr2012')
date
type(date)

date = pd.to_timedelta(2)
date

import datetime as dt
dtobj = dt.datetime.now()
dtobj



dtobj.year
dtobj.day
dtobj.month
dtobj.hour
dtobj.minute
dtobj.second

# # 0. Blogs
#
# - https://towardsdatascience.com/working-with-datetime-in-pandas-dataframe-663f7af6c587
# - https://www.analyticsvidhya.com/blog/2020/05/datetime-variables-python-pandas/
# - https://towardsdatascience.com/mastering-dates-and-timestamps-in-pandas-and-python-in-general-5b8c6edcc50c

# # 1. Reading / Converting to Timestamps

df = pd.DataFrame({"month": [2, 3], "day": [4, 5], "hour": [2, 3],"year": [2015, 2016]})
pd.to_datetime(df[["day", "month", "year"]])



# # 2. Generating Date Ranges : ```pd.date_range``` , ```pd.bdate_range```
#
# - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html#pandas.date_range
#
# - ```pandas.date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs)```[source]
#
# - Parameters :
#     - freq : possible values are **Y, M, D, W, Q, H, T for minutes, S**. Find more at 
#     https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases

# To make the creation of date sequences a convenient task, Pandas provides the date_range() method. It accepts a start date, an end date, and an optional frequency code:
#
# If we need timestamps on a regular frequency, we can use the ```date_range()``` and ```bdate_range()``` functions to create a DatetimeIndex. The default frequency for ```date_range``` is a ```calendar day``` while the default for ```bdate_range``` is a ```business day```:
#
# ```date_range``` and ```bdate_range``` make it easy to generate a range of dates using various combinations of parameters like ```start```, ```end```, ```periods```, and ```freq```. The **start and end dates are strictly inclusive**, so dates outside of those specified will not be generated:

pd.date_range(start='24/4/2020', end='24/5/2020', freq='D')

pd.date_range(start='24/4/2020', end='24/5/2021', freq='M')

pd.date_range(start='24/4/2020', end='24/5/2025', freq='Y')

start_date = pd.to_datetime('today').date()
start_date
start_date = dt.datetime.now().date()
start_date
dates_end = pd.date_range(start=start_date, periods=10, freq='D')
dates_end



# ### Creating a dataframe using date_range

start_date = pd.to_datetime('today').date()
start_date
dates_end = pd.date_range(start=start_date, periods=10, freq='Y')
dates_end

pd.DataFrame(dates_end, columns = ['YearEndDates'])

start_date = pd.to_datetime('today').date()
start_date
dates_end = pd.date_range(end=start_date, periods=10, freq='Y')
dates_end
pd.DataFrame(dates_end, columns = ['YearEndDates'])

# # 3. Indexing



# # 4. Date/Time components

# |Property| Description|
# |:-|:-|
# |year|The year of the datetime|
# |month|The month of the datetime|
# |day|The days of the datetime|
# |hour|The hour of the datetime|
# |minute|The minutes of the datetime|
# |second|The seconds of the datetime|
# |microsecond|The microseconds of the datetime|
# |nanosecond|The nanoseconds of the datetime|
# |date|Returns datetime.date (does not contain timezone information)|
# |time|Returns datetime.time (does not contain timezone information)|
# |timetz|Returns datetime.time as local time with timezone information|
# |dayofyear|The ordinal day of year|
# |day_of_year|The ordinal day of year|
# |weekofyear|The week ordinal of the year|
# |week|The week ordinal of the year|
# |dayofweek|The number of the day of the week with Monday=0, Sunday=6|
# |day_of_week|The number of the day of the week with Monday=0, Sunday=6|
# |weekday|The number of the day of the week with Monday=0, Sunday=6|
# |quarter|Quarter of the date: Jan-Mar = 1, Apr-Jun = 2, etc.|
# |days_in_month|The number of days in the month of the datetime|
# |is_month_start|Logical indicating if first day of month (defined by frequency)|
# |is_month_end|Logical indicating if last day of month (defined by frequency)|
# |is_quarter_start|Logical indicating if first day of quarter (defined by frequency)|
# |is_quarter_end|Logical indicating if last day of quarter (defined by frequency)|
# |is_year_start|Logical indicating if first day of year (defined by frequency)|
# |is_year_end|Logical indicating if last day of year (defined by frequency)|
# |is_leap_year|Logical indicating if the date belongs to a leap year|

# ## Data Preparation

df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
df
df.dtypes

# if column type is a string/object
# pd.DatetimeIndex(df['date']) returns Datetime type, which is chained with strftime
df['yyyy_ww1'] = pd.DatetimeIndex(df['date']).strftime('%Y-%U')
df
df.dtypes


# ### ```.strftime()```
# - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# if column type is a datetime
df['date'] = pd.to_datetime(df['date']) # Changing it to datatime object
df['yyyy_ww2'] = df['date'].dt.strftime('%Y-%U')
df
df.dtypes

df.loc[len(df.index)] = [dt.datetime.now(),np.NaN,np.NaN]
df

# - https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components

df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute
df['second'] = df['date'].dt.second
df['microsecond'] = df['date'].dt.microsecond
df
df.dtypes

# +
df['datepart'] = df['date'].dt.date
df['timepart'] = df['date'].dt.time

df['weekday'] = df['date'].dt.weekday
df['dayofweek'] = df['date'].dt.dayofweek
df['dayofyear'] = df['date'].dt.dayofyear
df['weekofyear'] = df['date'].dt.isocalendar().week
df['quarter'] = df['date'].dt.quarter
df
df.dtypes
# -

df['is_month_start'] = df['date'].dt.is_month_start
df['is_month_end'] = df['date'].dt.is_month_end
df['is_year_start'] = df['date'].dt.is_year_start
df['is_year_end'] = df['date'].dt.is_year_end
df['is_leap_year'] = df['date'].dt.is_leap_year
df
df.dtypes

# - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.day_name.html
# - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.normalize.html
# - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.round.html

# +
df['dayname'] = df['date'].dt.day_name()
df['monthname'] = df['date'].dt.month_name()
df['normalizeTime'] = df['date'].dt.normalize()
df['round'] = df['date'].dt.round(freq = "H")
df['floor'] = df['date'].dt.floor(freq = "H")
df['ceil'] = df['date'].dt.ceil(freq = "H")

df
df.dtypes
# -

df['mydate'] = pd.to_datetime(df[["day", "month", "year"]])
df



# # 5. Date Offsets
# - https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects

ts = pd.Timestamp("2014-01-01 09:00")
ts
type(ts)

ds = pd.to_datetime("2014-01-01")
ds
type(ds)

ts.day_name()
ds.day_name()

# ### Reset dataframe df

df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
df
df.dtypes
df.loc[len(df.index)] = [dt.datetime.now()]
df
df['date'] = pd.to_datetime(df['date'])
df
df.dtypes

# - **https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.tseries.offsets.DateOffset.html**

df['Off_Years'] =  df['date'] + pd.DateOffset(years=2)
df['Off_Months'] =  df['date'] + pd.DateOffset(months=2)
df['Off_Days'] =  df['date'] + pd.DateOffset(days=2)
df['Off_Weeks'] =  df['date'] + pd.DateOffset(weeks=2)
df['Off_Hours'] =  df['date'] + pd.DateOffset(hours=2)
df['Off_Mins'] =  df['date'] + pd.DateOffset(minutes=2)
df['Off_Secs'] =  df['date'] + pd.DateOffset(seconds=2)
df['Off_MilliSecs'] =  df['date'] + pd.DateOffset(milliseconds=2)
df
df.dtypes

# ### Reset dataframe df

df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
df
df.dtypes
df.loc[len(df.index)] = [dt.datetime.now()]
df
df['date'] = pd.to_datetime(df['date'])
df
df.dtypes

# ### The below code increment/decrement the date values based on +ve/-ve signs.
# The Offset Unit is provided as method
#
# - **https://pandas.pydata.org/pandas-docs/stable/reference/offset_frequency.html**

# +
df['Off_Years_End'] =  df['date'] + -2*pd.offsets.YearEnd()
df['Off_Years_Begin'] =  df['date'] + 2*pd.offsets.YearBegin()
df['Off_Months_End'] =  df['date'] + 2*pd.offsets.MonthEnd()
df['Off_Months_Begin'] =  df['date'] + 2*pd.offsets.MonthBegin()
df['Off_Quarter_End'] =  df['date'] + 2*pd.offsets.QuarterEnd()
df['Off_Quarter_Begin'] =  df['date'] + 2*pd.offsets.QuarterBegin()
df['Off_Weeks'] =  df['date'] + 2*pd.offsets.Week()
df['Off_Days'] =  df['date'] + 2*pd.offsets.Day()
df['Off_Bdays'] =  df['date'] + 2*pd.offsets.BDay()
df['Off_Hours'] =  df['date'] + 2*pd.offsets.Hour()
df['Off_Mins'] =  df['date'] + 2*pd.offsets.Minute()
df['Off_Secs'] =  df['date'] + 2*pd.offsets.Second()


df
df.dtypes
# -


