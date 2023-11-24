import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.pad(a,((2,5),(3,6)),'constant',constant_values=0)
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
d=np.pad(a,((1,6),(5,4)),'constant',constant_values=0)
print(a)
print(b)
print(d)
print(a[1,2])
