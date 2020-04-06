# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:19:35 2020

@author: abhi0
"""

import numpy as np

arr=np.arange(0.,10,1)
arr
print(arr)
print(arr[4])

print(arr*2)

arrcp=arr
arrcp

arrcp[2]=11.
arrcp
arr

arr2=arrcp[2]=12.
arr2
arrcp
arr

arr3=arr
arr3

arr3[3]=13.
arr3
arr
arrcp


np.sum(arr)
np.average(arr)
np.min(arr)
np.max(arr)
np.mean(arr)
# module 'numpy' has no attribute 'mode'
np.mode(arr)

# To create NumPy arrays of different datatypes
# array(), arange(), dtype
import numpy as np
a=np.array([1,2,3], dtype=np.int16)
print(a)
print(a.dtype)
# arange() - creates an array with evenly spaced numbers between start,inclusive and end,exclusive
ar=np.arange(0,10,1,dtype=np.int32)
print(ar)
print(ar.dtype)

b=np.array([1,2,3],dtype=np.float16)
print(b)
print(b.dtype)
br=np.arange(0,10,1,dtype=np.float64)
print(br)
print(br.dtype)

# To get the no. of axes, dimensions - ndim()
print(np.ndim(a))
print(np.ndim(ar))
print(np.ndim(b))
print(np.ndim(br))

print(a.ndim)
print(ar.ndim)
print(b.ndim)
print(br.ndim)

c=np.array([[1,2],[3,4],[5,6]])
print(np.ndim(c))
print(c.ndim)

d=np.array([[[1,2],[3,4],[5,6]],[[11,12],[13,14],[15,16]]])
print(d)
print(np.ndim(d))
print(d.ndim)

# To get the No. of Axes and No. of elements in each Axis - shape()
print(np.shape(a))
print(np.shape(b))
print(np.shape(c))
print(np.shape(d))

print(a.shape)
print(b.shape)
print(c.shape)
print(d.shape)

print(d.shape[0])
print(d.shape[1])
print(d.shape[2])

# to create NumPy arrays using ones() and zeros()
zero=np.zeros((2,3))
print(zero)
print(zero.shape)

one=np.ones((2,3,2))
print(one)
print(one.shape)

# Specify the dtype as the second argument to create array with specific dtype
zero=np.zeros((3,2,1),dtype=np.int16)
print(zero)
print(zero.shape)

one=np.ones((1,2,3),dtype=np.int16)
print(one)
print(one.shape)

one=np.ones((9),dtype=np.int16)
print(one)
print(one.shape)




