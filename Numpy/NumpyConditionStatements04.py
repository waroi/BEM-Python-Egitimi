import numpy as np

numpy_array=np.array([0,1,2,3,4,5,6,7,8,9])
boolean_array=numpy_array>=6
print(boolean_array)

print(numpy_array[boolean_array])
print(numpy_array<6)
print(numpy_array[numpy_array<6])