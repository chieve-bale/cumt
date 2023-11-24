import numpy as np
from math import cos,sin,pi
##单位统一为：长度mm，力N，应力MPa，默认E=206000MPa


class gan_jian:##定义杆件的原始单元刚度矩阵
    
    def __init__(self,E=206000,A=1,L=1):##类初始化
        self.E=E
        self.A=A
        self.i=E*A/L
        self.L=L
              
    def TT(self,a):##局部坐标系到整体坐标系的 坐标转换矩阵
        a=a*180/pi
        T=np.array([[cos(a)  ,sin(a)  ,0       ,0       ,0       ,0],\
                    [-sin(a) ,cos(a)  ,0       ,0       ,0       ,0],\
                    [0       ,0       ,1       ,0       ,0       ,0],\
                    [0       ,0       ,0       ,cos(a)  ,sin(a)  ,0],\
                    [0       ,0       ,0       ,-sin(a) ,cos(a)  ,0],\
                    [0       ,0       ,0       ,0       ,0       ,1]])
        
        return T
        
    def ff(self,gg):  ##输入杆件代码,代码为数字字符，输出刚度矩阵。按照课本P227表格顺序
        i=self.i
        L=self.L
        match gg:
            case '00':
                return np.array([[i        ,0         ,0         ,-i      ,0         ,0        ],\
                                 [0        ,12*i/L/L  ,6*i/L     ,0       ,-12*i/L/L ,6*i/L    ],\
                                 [0        ,6*i/L     ,4*i       ,0       ,-6*i/L    ,2*i      ],\
                                 [-i       ,0         ,0         ,-i      ,0         ,0        ],\
                                 [0        ,-12*i/L/L ,-6*i/L    ,0       ,12*i/L/L  ,-6*i/L   ],\
                                 [0        ,6*i/L     ,2*i       ,0       ,-6*i/L    ,4*i      ]])
            case '01':
                return [[]]
            case '02':
                return [[]]
        
print(gan_jian().ff('00'))
print(gan_jian().TT(45))




aa=np.zeros((3,3))

print(aa)
