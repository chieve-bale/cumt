import numpy as np
from math import cos,sin,pi
##单位统一为：长度mm，力N，应力MPa，默认E=206000MPa ，角度默认 °（逆时针为正）


class gan_jian:##定义杆件的原始单元刚度矩阵
    
    def __init__(self,xu_hao=0,jie_dian=(0,0),E=206000,A=1,I=1,L=1,a=0):##类初始化
        self.xu_hao=xu_hao
        self.jiie_dian=jie_dian
        self.E=E
        self.A=A
        self.I=I
        self.i=E*A/L
        self.L=L
        self.a=a
              
    def TT(self):##局部坐标系到整体坐标系的 坐标转换矩阵
        a=self.a*180/pi
        s=-0.894
        c=0.447   
        T1=np.array([[c,s,0,0,0,0],\
                     [-s,c,0,0,0,0],\
                     [0,0,1,0,0,0],\
                     [0,0,0,c,s,0],\
                     [0,0,0,-s,c,0],\
                     [0,0,0,0,0,1]])
        T2=np.array([[cos(a)  ,sin(a)  ,0       ,0       ,0       ,0],\
                    [-sin(a) ,cos(a)  ,0       ,0       ,0       ,0],\
                    [0       ,0       ,1       ,0       ,0       ,0],\
                    [0       ,0       ,0       ,cos(a)  ,sin(a)  ,0],\
                    [0       ,0       ,0       ,-sin(a) ,cos(a)  ,0],\
                    [0       ,0       ,0       ,0       ,0       ,1]])
        
        return T1
        
    def jv_bu_zuo_biao_xi(self,gg='00'):  ##输入杆件代码,代码为数字字符，输出局部坐标系刚度矩阵。按照课本P227表格顺序
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

    def zheng_ti_zuo_biao_xi(self):
        return self.TT().T@self.jv_bu_zuo_biao_xi()@self.TT()

gj=gan_jian(I=40000000000,A=400000,E=210000,L=5590,xu_hao=1,a=0)
t=gj.TT()
k=gj.jv_bu_zuo_biao_xi()
print(t.T,k,t)
print(t.T@k@t)

print(gj.zheng_ti_zuo_biao_xi())




##a=np.array([[150.3,0,0,-150.3,0,0],[0,5.771,16.13,0,-5.771,16.13],[0,16.13,60.1,0,-16.13,30.1],[-150.3,0,0,150.3,0,0],[0,-5.771,-16.13,0,5.771,-16.13],[0,16.13,30.1,0,-16.13,60.1]])

##aa=np.zeros((3,3))
