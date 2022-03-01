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

# ## Prepared by Abhishek Kumar
# #### https://bit.ly/AKSLinkedIn

# +
# To get multiple outputs in the same cell

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# +
# Import libraries

import pandas as pd
import numpy as np
import sqlite3 as sql
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# +
# Creating a database for Vauld

conn = sql.connect('vauld.db')
# -

# ## -----------------------------------------------------------------------------------------------------------------------------
# ## Part 1
# ## -----------------------------------------------------------------------------------------------------------------------------

# Question 1
# ![image.png](attachment:image.png)

# ### Data Preparation

data = {'vendor_id':[1,2,3,4,5,6],
       'name':['Schmendor','Parts_r_us','Vendor_king','Mathews','Victor','Burger_man'],
       'contract_sign_dt':['2018-9-1','2018-9-3','2018-10-11','2018-8-21','2018-8-13','2018-10-29'],
       'total_spend':[34324,23455,77654,23334,94843,23444]}
vendor_spend = pd.DataFrame(data)
vendor_spend['contract_sign_dt'] = pd.to_datetime(vendor_spend.contract_sign_dt)

vendor_spend.shape
vendor_spend

# ### Python Implementation

vendor_spend[vendor_spend.total_spend>np.median(vendor_spend.total_spend)]

# ### SQL Implementation

# Creating the weather table in vauld database
vendor_spend.to_sql('vendor_spend',conn,if_exists='replace',index=False)

# Query prepartion
query = '''

select vendor_id,name,contract_sign_dt,total_spend
from (select *, percent_rank() over (order by total_spend) as percntile from vendor_spend) as per
where percntile > 0.5

'''

# +
# Passing the query to vauld db for execution

result = pd.read_sql(query,conn)
result
# -

# **Result** - Vendor 1, 3 and 5 are the top 50% spender



# Question 2
# ![image.png](attachment:image.png)

# ### Data Preparation

data = {'id':[1,2,3,4,5,6],
       'record_dt':['2015-1-1','2015-1-2','2015-1-3','2015-1-4','2015-1-5','2018-1-6'],
       'temperature':[10,25,20,30,28,27]}
weather = pd.DataFrame(data)
weather['record_dt'] = pd.to_datetime(weather.record_dt)

weather.shape
weather

# ### Python Implementation

# Python Implementation
weather_py = weather.copy()
weather_py['prev_temp'] = weather_py.sort_values('record_dt').temperature.shift(1)
weather_py[weather_py.temperature > weather_py.prev_temp]['id'].to_frame()

# ### SQL Implementation

# Creating the weather table in vauld database
weather.to_sql('weather',conn,if_exists='replace',index=False)

# Query prepartion
query = '''

select id
from (select *, lag(temperature) over (order by record_dt) as prev_temp from weather) as lag
where temperature > prev_temp


'''

# +
# Passing the query to vauld db for execution

result = pd.read_sql(query,conn)
result
# -

# **Result** - The days with ID value 2 and 4 have higher temperatures than their previous days respectively.

# ## -----------------------------------------------------------------------------------------------------------------------------
# ## Part 2
# ## -----------------------------------------------------------------------------------------------------------------------------

# Question
# ![image.png](attachment:image.png)

# ![image-2.png](attachment:image-2.png)
# ![image-3.png](attachment:image-3.png)

# ### Data Preparation

sessions = pd.read_excel('./one.xlsx', sheet_name='sessions')
sessions['Started_At'] = pd.to_datetime(sessions.Started_At)
sessions['Ended_At'] = pd.to_datetime(sessions.Ended_At)
sessions

conversions = pd.read_excel('./one.xlsx', sheet_name='conversions')
conversions['converted_at'] = pd.to_datetime(conversions.converted_at)
conversions['customer_id'] = conversions.customer_id.astype('int')
conversions

# Creating the sessions and conversions table in vauld database
sessions.to_sql('sessions',conn,if_exists='replace',index=False)
conversions.to_sql('conversions',conn,if_exists='replace',index=False)


# user defined function to execute query
def run(query, conn=conn):
    # Passing the query to vauld db for execution
    result = pd.read_sql(query,conn)
    return result


# ### SQL Implementation

# Query prepartion : Data overview
query = '''

select s.* , case when converted_at between Started_At and Ended_At then 1 else 0 end as flag
from sessions s left join conversions c
on s.customer_id = c.customer_id

'''

run(query)

# **Question 1 - how many users it helped convert**

# +
# Query prepartion : Conversion Rate by Campaign

query = '''

select UTM_Campaign, count(distinct Customer_Id) as targeted_customer_count, sum(flag) as conversion_count,
sum(flag)*100 / count(distinct Customer_Id) as conversion_pct
from (
select s.* , case when converted_at between Started_At and Ended_At then 1 else 0 end as flag
from sessions s left join conversions c
on s.customer_id = c.customer_id )
group by UTM_Campaign

'''
# -

run(query)

# +
# Query prepartion : Conversion Rate by Medium 

query = '''

select UTM_Medium, count(distinct Customer_Id) as targeted_customer_count, sum(flag) as conversion_count,
sum(flag)*100 / count(distinct Customer_Id) as conversion_pct
from (
select s.* , case when converted_at between Started_At and Ended_At then 1 else 0 end as flag
from sessions s left join conversions c
on s.customer_id = c.customer_id )
group by UTM_Medium

'''
# -

run(query)

# +
# Query prepartion : Conversion Rate by Source 

query = '''

select UTM_Source, count(distinct Customer_Id) as targeted_customer_count, sum(flag) as conversion_count,
sum(flag)*100 / count(distinct Customer_Id) as conversion_pct
from (
select s.* , case when converted_at between Started_At and Ended_At then 1 else 0 end as flag
from sessions s left join conversions c
on s.customer_id = c.customer_id )
group by UTM_Source

'''
# -

run(query)

# +
# Query prepartion : Conversion Rate by Campaign, Medium, Source

query = '''

select UTM_Campaign, UTM_Medium, UTM_Source, count(distinct Customer_Id) as targeted_customer_count,
sum(flag) as conversion_count, sum(flag)*100 / count(distinct Customer_Id) as conversion_pct
from (
select s.* , case when converted_at between Started_At and Ended_At then 1 else 0 end as flag
from sessions s left join conversions c
on s.customer_id = c.customer_id )
group by UTM_Campaign, UTM_Medium, UTM_Source

'''
# -

run(query)

# - **Result - Based on the Last Interaction Attribution Model, the last touchpoint is provided the conversion credit**
# - **The above result shows the conversion percentage for different sources and mediums for each campaign**
# - **Youtube through Social video is 100% performant**



# **Question 2 - how many touch points it takes a user to get converted**

# +
# Query prepartion : Touch points for each customer

query = '''

select customer_id, count(*) as count_touch_point
from (
select c.* , case when converted_at between Started_At and Ended_At then 1 else 0 end as flag
from conversions c left join sessions s
on s.customer_id = c.customer_id )
group by customer_id

'''
# -

run(query)

# **Result** - The customers listed with their touch-points till conversion



# ## -----------------------------------------------------------------------------------------------------------------------------
# ## Part 3
# ## -----------------------------------------------------------------------------------------------------------------------------

# ![image.png](attachment:image.png)

# ## Expected Data Model
#
# 1. Customer-Transaction Relationship
#     - customer_id, tran_id
# 2. Transactions
#     - tran_id, token, tran_amt, tran_type, network
#
# - Consider transactions only after the launch

# ## Descriptive stats to find performance of the new network
#
# At the end of Week 1
# 1. %ge of transactions (in terms of frequency and Amount) across different network
# 2. %ge of bep-20 transactions (in terms of frequency and Amount) across different transaction_type
# 3. %ge of customers using bep-20 out of customers who did a transaction
# 4. %ge of Re-activated customers for this week comparing to previous 2-3 weeks
# 5. %ge increase in Total transaction (frequency and volume) for this week comparing to previous 2-3 weeks
# 6. %ge of customers using bep-20 out of customers who did a transaction.
#     and this can be done across GENDER, AGE, GEOGRAPHY, Device-OS, etc
#
# Daily based
# 1. Plot Daily transactions (in terms of Frequency and Total Volume) in a line chart for different networks
# 2. Analyze any impact (decrease/increase) on daily churn rates for this week compared to previous 2-3 weeks 

#
#
#

# What changes will you make for future releases based on your learnings?
#
#

# - If there is no significant increase in TOTAL VOLUMES/Transacting CUSTOMERs, then a customer survey or general market data can be analysed before coming up with a feature., given the constraints in the question.


