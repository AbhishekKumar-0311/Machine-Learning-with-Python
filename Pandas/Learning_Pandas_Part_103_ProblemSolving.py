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

# ## 0. Data

df1 = pd.DataFrame({'id': [1,2],
                   'name': ['a','b'],
                   'prem1' : [100,280],
                   'prem2' : [np.NaN,180],
                   'prem3' : [300,np.NaN],
                   'disc1' : [20,40],
                   'disc2' : [np.NaN,30],
                   'disc3' : [50,np.NaN],})
df1

df1.iloc[::-1,::-1]

# +
d = {"salesperson":["Nico", "Carlos", "Juan", "Nico", "Nico", "Juan", "Maria", "Carlos"], "beer_item":[10, 120, 130, 200, 300, 550, 12.3, 200],
    "wine_item":[10, 120, 130, 200, 300, 550, 12.3, 200], "spirit_item":[10, 120, 130, 200, 300, 550, 12.3, 200]}
df = pd.DataFrame(d)
df

drink = 'wine'
#drink = ['wine','beer']
df[[f"salesperson",f"{drink}_item"]]
# -

# ## 1. Validate EMAIL ID

# Valid email ID
# Description
# Consider that email IDs are supposed to be for the following format:
# username@website.extension.
# Here, there are three conditions to keep in mind:
# 1. The username can only contain characters 0-9, a-z and A-Z.
# 2. The website name can contain only characters a-z
# 3. The extension can have 2 or 3 alphabets(a-z).
#
# Given an email ID, you have to determine if it is valid or not.
#
# Sample Input:
# prerna@upgrad.com
#
# Sample Output:
# valid

# +
import re

def checkmail(email):
    #complete the function
    #the function should return the strings "invalid" or "valid" based on the email ID entered
    mo = re.search(r'\A[a-zA-Z0-9]+@[a-z]+\.[a-z]{2,3}$',email)
    if mo == None:
        return 'invalid'
    else:
        return 'valid'



email='hi*gail.com'
print(checkmail(email))
# -

# ## 2. Flatten a list

# Flatten a list
# Description
# Given a nested list, write python code to flatten the list.
# Note: The input list will strictly have 2 levels, i.e. the list will be of the form [[1,2],[3,4]]. Inputs like [1,[2,3]] and [[1,[2,3],4],5] are not applicable.
#
# For example: If the input list is :
# [[1,2,3],[4,5],[6,7,8,9]]
# Then the output should be:
# [1,2,3,4,5,6,7,8,9]

# +
lst = [[1,2,3],[4,5],[6,7,8,9]]

fl = [y for x in lst for y in x]
fl
# -

# ## 3. Calculate squares conditionally

#
# Description
# Given a list of positive integers, you have to find numbers divisible by 3 and replace them with their squares. 
# For example, consider the list below:
# Input: [1,2,3,4,5,6]
# The output for the above list would be: [1,2,9,4,5,36]. Because 3 and 6 were divisible by 3, these numbers were replaced with their squares.

lst =  [1,2,3,4,5,6]
lst

sq_lst = [x**2 if x % 3 == 0 else x for x in lst]
sq_lst

# ## 4. A weird sum
# Description
#
#     Write a program that computes the value of n+nn+nnn+nnnn with a given digit as the value of n.
#     For example, if n=9 , then you have to find the value of 9+99+999+9999.

# +
inp=input()

sums = int()
for i in range(1,5):
    s = ''
    for j in range(i):
        s += inp
    sums += int(s)
    print(s)
print(sums)

# +
n=input()
n1 = int( "%s" % n)
n2 = int( "%s%s" % (n,n) )
n3 = int( "%s%s%s" % (n,n,n) )
n4 = int( "%s%s%s%s" % (n,n,n,n) )

print (n1+n2+n3+n4)
# -
# ## 5. Frequent Letters
#
# Description
#
#     Given a string, you have to find the first n most frequent characters in it.
#
#     You have to print these n letters in alphabetically sorted order.
#
#     The input will contain two lines, the first line will contain a string and the second line will contain the letter n.
#
#     The output should be a list of n most frequent letters in alphabetically sorted order.
#
#     Note: If there are two letters with the same frequency, then the alphabetically preceding alphabet should be picked first. (For example, in "aabbccc", if n=2, then output list would have c and a.)
#
#     Sample Input:
#
#     ddddaacccb
#
#     3
#
#     Sample Output:
#
#     ['a', 'c', 'd']

# +
string=input()
n=int(input())
#write your code here

#''.join(sorted(test_str))
uniq_char = sorted(list(set(string)), reverse=True)
#uniq_char
#type(uniq_char)

d = {}
#type(d)

for c in uniq_char:
    counter = string.count(c)
    #c
    #counter
    d[counter] = c
#d

sorted_dict = {r: d[r] for r in sorted(d, reverse=False)}
sorted_dict

ls = list(sorted_dict.values())
print(ls[-n:])
# -

string=input()
n=int(input())
import collections
out=[collections.Counter(string).most_common(i+1)[i][0] for i in range(n)]
out.sort()
print(out)

# ## 6. 2D array
# Description
#     
#     Write Python code which takes 2 numbers x and y as input and generates a 2-dimensional numpy array where value in the i-th row and j-th column of the array should be (i+j)/2.
#
#     Note: i=0,1,...x-1 and j=0,1....,y-1
#         The input will have two lines with x and y respectively.
#         The output should be a 2D numpy array.
#
# Sample Input:
#
# 3
#
# 4
#
# Sample Output:
#
# [[0.  0.5 1.  1.5]
#  [0.5 1.  1.5 2. ]
#  [1.  1.5 2.  2.5]]

x=3
y=4
arr = np.ones([x,y])
arr

arr1 = np.empty([x,y])
arr1

for i in range(x):
    for j in range(y):
        arr[i,j] = (i+j)/2
arr

x=int(input())
y=int(input())
from numpy import zeros
a = zeros([x,y])
for row in range(x):
    for col in range(y):
        a[row][col]= (row+col)/2
print(a)

# ## 7. 8th Highest Purchase
# - One complex sql query- 2 table are there, Table1(cust_id,Name) Table2(cust_id,Transaction_amt)
# - Write a query to return the name of customers with 8th highest lifetime purchase.
#

# +
rows = [['1','Abhishek'],
        ['2','Anusha'],
        ['3','BalaJi']]

columns = ['id','name']

cust = pd.DataFrame(rows, columns=columns)
cust

# +
data_dict = {'id' : ['1','1','2','3','1','2','3','1','3','3','3','2'],
            'amt' : [100,50,200,300,400,500,20,10,100,180,30,600]}

trans = pd.DataFrame(data_dict)
trans

# +
# create a list for column 1
id = ['1','1','2','3','1','2','3','1','3','3','3','2']

# create a list for column 2
amt = [100,50,200,300,400,500,20,10,100,180,30,600]

list_of_tuples = list(zip(id, amt)) 
list_of_tuples

transtest = pd.DataFrame(list_of_tuples, columns = ['id','amt'])
transtest
# -

# Method 1 : Creating an Aggregate table and renaming columns
trans_agg = trans.groupby('id', as_index=False)['amt'].sum().rename(columns = {'amt': 'TotAmt'})
trans_agg

# Method 2 : Creating an Aggregate table with NamedAggregate
trans.groupby('id', as_index=False).agg(TotAmount = pd.NamedAgg('amt','sum'))

all = pd.merge(cust,trans_agg, on='id')
all

all.sort_values('TotAmt', ascending=False)

# Here 2nd Highest is found, by passing row index = 1 on the sorted data
all.sort_values('TotAmt', ascending=False).reset_index().drop('index', axis=1).iloc[[1]]

# Here 2nd highest is found, by creating a Rank on Salary and then filtering it
all['rnk'] = all['TotAmt'].rank()
all[all.rnk==2]

all['TotAmt'].nlargest(2)

all.nlargest(2,['TotAmt'])

# ## 9. To replace values greater than 1000 with Null for all the columns or numeric columns in dataframe
#

# +
# Data Preparation
id = [1,2,3,4,5]
prod1 = [100,np.NaN,250,225,300]
prod2 = [400,100,250,np.NaN,60]

list_of_tuples = list(zip(id, prod1,prod2)) 
list_of_tuples

data = pd.DataFrame(list_of_tuples, columns = ['id','prod1','prod2'])
data
# -

data['prod11'] = data['prod1'].apply(lambda x : 0 if x >= 250 else x)
data

data.applymap(lambda x : 0 if x >= 250 else x)


