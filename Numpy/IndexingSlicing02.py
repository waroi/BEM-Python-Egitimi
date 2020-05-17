import numpy as np

numpy_array=np.array([0,1,2,3,4,5,6,7,8,9])

#arange(başlama,bitiş,artış)

print(np.arange(0,10,3))
print(np.arange(5))
print(np.arange(3,8))

#[satır,sütun]

numpy_array=numpy_array.reshape(5,2)
print(numpy_array)
print(numpy_array[0])
print(numpy_array[0:3])
#[:,:]

print(numpy_array[:,0])
print(numpy_array[:,0:2])

print(numpy_array[3,1])

print(numpy_array[::-1])

print(np.zeros((6,8)))
print(np.zeros((5,6,8)))

print(np.ones((5,8)))
print(np.ones((5,5,8)))

print(np.eye(6))

print(np.concatenate([numpy_array,numpy_array], axis=0))
print(np.concatenate([numpy_array,numpy_array], axis=1))
