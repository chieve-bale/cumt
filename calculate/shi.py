import numpy as np
import json

a=199

ty=type(a)
print(ty)
if ty==int or (ty==list and len(a)==1) or (ty==list and len(a)==2 and a[0]==a[1]) :
    print('int')
                
if ty==list and len(a)==2:
    print('list')
