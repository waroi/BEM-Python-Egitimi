import numpy as np

python_list=[0,1,2,3,4,5,6,7,8,9]
numpy_array=np.array([0,1,2,3,4,5,6,7,8,9])

print("python listesi:",python_list)
print("numpy array:   ",numpy_array)

print(numpy_array.ndim)

numpy_array2=np.array([[0,1,2,3,4,5,6,7,8,9]])
print(numpy_array2)
print(numpy_array2.ndim)

print(numpy_array.shape)
print(numpy_array2.shape)

print(numpy_array.reshape(5,2))
print(numpy_array2.reshape((10,)))

print(numpy_array)
print(numpy_array2)

numpy_array=numpy_array.reshape(5,2)
numpy_array2=numpy_array2.reshape(10,)

print("yeni numpy array:",numpy_array)
print("yeni numpy arry2:",numpy_array2)
