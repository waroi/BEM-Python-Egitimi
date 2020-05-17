import numpy as np

a=np.floor(np.random.random((3,4)))
print(a)
a=np.floor(10*np.random.random((3,4)))
print(a)

print(a.ravel())
print(a.reshape(6,2))

print(a.T)

print(a.ravel(order='C'))
print(a.ravel(order='F'))
print(a.ravel(order='A'))
print(a.ravel(order='K'))