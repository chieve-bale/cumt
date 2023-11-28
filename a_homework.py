import numpy as np
import math
c=round(math.sin(math.pi*45/180),4)
s=round(math.sin(math.pi*45/180),4)
EA=2400000
i=12000
L=6
T=np.array([[ c, s, 0, 0, 0, 0],\
                         [-s, c, 0, 0, 0, 0],\
                         [ 0, 0, 1, 0, 0, 0],\
                         [ 0, 0, 0, c, s, 0],\
                         [ 0, 0, 0,-s, c, 0],\
                         [ 0, 0, 0, 0, 0, 1]])
k=np.array([[EA/L     ,0         ,0         ,-EA/L   ,0         ,0        ],\
                                 [0        ,12*i/L/L  ,6*i/L     ,0       ,-12*i/L/L ,6*i/L    ],\
                                 [0        ,6*i/L     ,4*i       ,0       ,-6*i/L    ,2*i      ],\
                                 [-EA/L    ,0         ,0         ,EA/L    ,0         ,0        ],\
                                 [0        ,-12*i/L/L ,-6*i/L    ,0       ,12*i/L/L  ,-6*i/L   ],\
                                 [0        ,6*i/L     ,2*i       ,0       ,-6*i/L    ,4*i      ]])
print(T)
print(T.T)
print(k)
print(T.T@k@T)