"""
Name: Trever Cluney
Date: 1.31.22
Email: tlcluney@dmacc.edu
Overview: Learning to use numpy arrays
"""
import numpy as np

array1 = np.array([[10, 15, 20], [2, 3, 4], [9, 14.5, 18]])
array2 = np.array([[1, 2, 5], [8, 0, 12], [11, 3, 22]])

print(array1)
print(array1.shape)
array1_slice = array1[0:2, 0:2]
print(array1_slice)
array1_even = array1 % 2 == 0
print(array1_even)

array_sum = np.add(array1, array2)
print(array_sum)
array_sum = np.multiply(array1, array2)
print(array_sum)

print(array2.sum())
print(array2.prod())
print(array2.max())
print(array2.min())
