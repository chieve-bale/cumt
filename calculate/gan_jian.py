import numpy as np
import math
import json

class gan_jian:##定义杆件的原始单元刚度矩阵
    
    def __init__(self,xu_hao=0,jie_dian=[0,0],E=206000,A=1,I=1,L=1,a=0,cos=0,sin=0):##类初始化
        self.xu_hao=xu_hao    ##杆件序号
        self.jie_dian=jie_dian##杆件节点
        self.E=E              ##弹性模量
        self.A=A              ##截面面积
        self.I=I              ##截面惯性矩
        self.i=E*I/L          ##杆件线刚度
        self.EA=E*A
        self.L=L              ##杆件长度
        self.a=a              ##杆件角度，顺时针为正
        if cos==0 and sin==0:
            self.cos=math.cos(a/180*math.pi)
            self.sin=math.sin(a/180*math.pi)
        else:
            self.sin=sin          ##杆件角度正弦
            self.cos=cos          ##杆件角度余弦
             
    def TT(self):##局部坐标系到整体坐标系的 坐标转换矩阵
        s=self.sin
        c=self.cos
        return np.array([[ c, s, 0, 0, 0, 0],\
                         [-s, c, 0, 0, 0, 0],\
                         [ 0, 0, 1, 0, 0, 0],\
                         [ 0, 0, 0, c, s, 0],\
                         [ 0, 0, 0,-s, c, 0],\
                         [ 0, 0, 0, 0, 0, 1]])
        
    def jv_bu_zuo_biao_xi(self,gg='00'):  ##输入杆件代码,代码为数字字符，输出局部坐标系刚度矩阵。按照课本P227表格顺序
        i=self.i
        L=self.L
        EA=self.EA
        match gg:
            case '00':
                return np.array([[EA/L     ,0         ,0         ,-EA/L   ,0         ,0        ],\
                                 [0        ,12*i/L/L  ,6*i/L     ,0       ,-12*i/L/L ,6*i/L    ],\
                                 [0        ,6*i/L     ,4*i       ,0       ,-6*i/L    ,2*i      ],\
                                 [-EA/L    ,0         ,0         ,EA/L    ,0         ,0        ],\
                                 [0        ,-12*i/L/L ,-6*i/L    ,0       ,12*i/L/L  ,-6*i/L   ],\
                                 [0        ,6*i/L     ,2*i       ,0       ,-6*i/L    ,4*i      ]])
            case '01':
                return [[]]

    def zheng_ti_zuo_biao_xi(self):
        resault=self.TT().T@self.jv_bu_zuo_biao_xi()@self.TT()
        # print(self.jv_bu_zuo_biao_xi())
        return resault