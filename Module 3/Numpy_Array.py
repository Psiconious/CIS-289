import numpy as np

my_narray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]])
print(my_narray)

# Output the shape of the array
print(my_narray.shape)
# Output the number of items in the array
print(my_narray.size)
# Output the datatype of the array items
print(my_narray.dtype)
# Returns the maximum value in the entire array
print(my_narray.max())
# Sums the entire array
print(my_narray.sum())
print("")
# Returns the maximum value on axis 0
print(my_narray.max(axis=0))
# Sums (collapses) the array along axis 1
print(my_narray.sum(axis=1))
my_narray_slice = my_narray[1:3, 1:3]
print(my_narray_slice)
my_array_divide_by_3 = my_narray % 3==0
print(my_array_divide_by_3)

array_1 = np.array([[1,2],[3,4]])
array_2 = np.array([[3,4],[5,6]])

array_sum = np.add(array_1,array_2)
print(array_sum)
array_sum = np.multiply(array_1,array_2)
print(array_sum)
