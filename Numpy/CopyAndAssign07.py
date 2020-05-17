import numpy as np

a=np.arange(12)
b=a
print(b is a)
b.shape=4,3
print(a.shape)

c=a.view()
print(c is a)
print(c.base is a)
print(c.flags.owndata)
c.shape=6,2
print(a.shape)
c[4,1]=1453 
print(a)

d=a.copy()
print(d is a)
print(d.base is a)
d[1,1]=1071
print(a)