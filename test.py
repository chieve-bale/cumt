##import json
##a=[{'xu_hao':0,'jie_dian':(0,1),'E':210000,'A':400000,'I':40000000000,'L':5000,'a':0,'cos':0,'sin':0},{'xu_hao':1,'jie_dian':(1,2),'E':210000,'A':400000,'I':40000000000,'L':5590,'a':0,'cos':0.447,'sin':-0.895}]
##with open('gan_jian_lib.json','w') as f:
##    json.dump(a,f,ensure_ascii=False, indent=4)
import numpy as np
k=np.array([[202.67,-57.79,14430],[-57.79,129.42,-12950],[14430,-12950,127310000]])
f=np.array([[50000,30000,20000000]]).T
kk=np.linalg.inv(k)
print(k)
print(f)
print(f.T)

d=kk@f
print(d)
[[1,2,3]]
