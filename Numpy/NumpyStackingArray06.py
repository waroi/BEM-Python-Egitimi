import numpy as np

a=np.floor(10*np.random.random((3,3)))
print(a)
b=np.floor(10*np.random.random((3,3)))
print(b)


print(np.stack(((a,b))))

print(np.vstack((a,b)))

print(np.hstack((a,b)))

print(np.stack((a,b), axis=-3))

c=np.floor(10*np.random.random((4,14)))
print(c)

print(np.array_split(c,4))
print(np.array_split(c,4,axis=1))

print(np.hsplit(c,2))
print(np.vsplit(c,2))