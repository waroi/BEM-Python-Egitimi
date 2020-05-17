# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:30:24 2020

@author: Enes AYDIN
"""


import numpy as np

numpy_array=np.array([1,2,3,4,5,6,7,8,9])
numpy_array=numpy_array.reshape(3,3)
print(numpy_array)

print(numpy_array.max())
print(numpy_array.min())

print(numpy_array.sum())
print(numpy_array.sum(axis=1))
print(numpy_array.sum(axis=0))

print(numpy_array.mean())
print(np.median(numpy_array))
print(numpy_array.var())
print(numpy_array.std())

numpy_array2=np.array([9,8,7,6,5,4,3,2,1])
numpy_array2=numpy_array2.reshape(3,3)

print(np.add(numpy_array,numpy_array2))
print(np.subtract(numpy_array2,numpy_array))
print(np.multiply(numpy_array,  numpy_array2))
print(np.dot(numpy_array,numpy_array2))

print(np.sin(numpy_array))
print(np.cos(numpy_array))
print(np.sqrt(numpy_array))
print(np.exp(numpy_array)) #e=2.71
print(np.log(numpy_array)) 

print(numpy_array.T)
print(numpy_array2.T)


print(numpy_array+numpy_array2)
print(numpy_array+8)
print(numpy_array2-numpy_array)
print(numpy_array*numpy_array2)
print(numpy_array*5)
print(numpy_array2/numpy_array)

