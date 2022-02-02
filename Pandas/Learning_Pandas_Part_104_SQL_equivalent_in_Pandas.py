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

# +
# To get multiple outputs in the same cell

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# %matplotlib inline
# -

import sqlite3 as sql

import pandas as pd
import numpy as np
import sqlite3 as sql
# conn = sql.connect('default.db')
import matplotlib.pyplot as plt



# I got this data at http://ourairports.com/data/.

airport = pd.read_csv('./data/airports.csv')
run = pd.read_csv('./data/runways.csv')

airport.shape
run.shape


# df_return = sqldb(airport,'airport',query,conn=, direct_run=)
def sqldb(sql_query, conn = sql.connect('default.db'), direct_run = 1, df = df, sql_tbl = sql_tbl ):
    ''' df -> pandas dataframe
        sql_tbl -> equivalent table in Db
        sql_query -> query to be executed in sql env
        conn -> connection to database: deafult db is set to default.db
        direct_run -> indicates whether the query needs to be executed on existing table or needs to be re-created '''
    if direct_run == 0:
        cursor = conn.cursor()
        drop_query = "DROP TABLE IF EXISTS " + sql_tbl
        cursor.execute(drop_query)
        df.to_sql(sql_tbl,conn)
    dfinit = pd.read_sql(sql_query,conn)
    return dfinit


# +
conn = sql.connect('default.db')
direct_run = 1
df_arg = airport
sql_tbl = 'airport'
query = 'select * from airport limit 10'

df_return = sqldb(query,conn,direct_run=1)
df_return
# -

# %reset?

airport.to_sql('airport',conn)
query = 'select * from airport limit 10'
dfinit = pd.read_sql(query,conn)
dfinit

ap = airport.copy()
ap.head(3)









# # Sample SQL 
# - SELECT… FROM… WHERE…
# - GROUP BY… HAVING…
# - ORDER BY…
# - LIMIT… OFFSET…

# ##  SELECT…  FROM…

# +
# SELECT… < *, Few> FROM…

ap                                 # SELECT *
ap.head(3)                         # LIMIT
ap[['ident','type','name']]        # SELECT Few
ap.type.unique()                   # SELECT DISTINCT
list(ap.type.unique())             # SELECT DISTINCT -> to get distinct values as a list
ap.type.nunique()                  # SELECT DISTINCT COUNT
len(ap.type.unique())              # SELECT DISTINCT COUNT
# -

# ## SELECT… FROM… WHERE… ORDER BY... and LIMIT…

# +
# SELECT… FROM… WHERE… ORDER BY… and LIMIT…

ap[['ident','type','name']][ap.type == 'small_airport']                         # SELECT Few & WHERE
ap[['ident','type','name']][ap.type == 'small_airport'].head(3)                 # SELECT Few & WHERE and LIMIT
ap[ap.type == 'small_airport'].head(3)                                          # SELECT ALL & WHERE (==) and LIMIT
ap[ap.type.isin(['small_airport','heliport'])][['ident','type','name']].head(3) # SELECT Few & WHERE (.isin()) and LIMIT
ap[ap.type == 'small_airport'].head(3).sort_values('name', ascending = False)   # SELECT ALL & WHERE (==) and LIMIT and ORDER BY
ap[ap.type == 'small_airport'].sort_values('name', ascending = False).head(3)   # SELECT ALL & WHERE (==) and LIMIT and ORDER BY

# -

# ## SELECT… FROM… WHERE… GROUP BY... HAVING... ORDER BY... and LIMIT…

run.head(3)

run.airport_ref.value_counts()

t = run.groupby('airport_ref')

t.get_group('3754')

t.first()

t.head(1)

t.ngroup()

t.nth(2)

t.size()

t.all()

t.nunique()

t.describe()











ap = ap.iloc[:,0:6]
ap.head(3)
len(ap)

ap.dtypes

list((ap.latitude_deg.min(),ap.latitude_deg.max(),ap.latitude_deg.mean()))


ap.agg({'latitude_deg': ['min','max','mean']})
ap.agg({'latitude_deg': ['min','max','mean']}).T

ap.agg({'latitude_deg': ['count','min','max','mean'],'longitude_deg': ['count','min','max','mean']})
ap.agg({'latitude_deg': ['count','min','max','mean'],'longitude_deg': ['count','min','max','mean']}).T

ap.min()


