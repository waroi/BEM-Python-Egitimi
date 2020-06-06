import numpy as np
import pandas as pd

#seriler=pd.Series(data,index)
#data=sabit bir değer,liste,numpy dizisi,dictionary(sözlük)

sayılar=[0,1,2,3,4,5,6,7,8,9]
numpy_array=np.array(sayılar)
print(numpy_array)
seriler=pd.Series(data=sayılar)
print(seriler)

# my_index=['a','b','c','d','e','f','g','h','i','j']
# seriler=pd.Series(data=sayılar,index=my_index,dtype=int)
# print(seriler)

# sözlük={'a':0,'b':1,'c':2,'d':3}
# seriler=pd.Series(data=sözlük)
# print(seriler)

# print(seriler.ndim) #serinin boyutu
# print(seriler.dtype) #serinin data tipi
# print(seriler.shape) #serinin boyutu(satır ve sütun)