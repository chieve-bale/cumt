import numpy as np
import math
import json
##添加对cos^2+sin^2=1的验证，添加错误提示
class gan_jian:##定义杆件的原始单元刚度矩阵
    
    def __init__(self,xu_hao=0,jie_dian=[0,0],E=206000,A=1,I=1,L=1,a=0,cos=0,sin=0,lian_jie=[0,0]):##类初始化
        self.xu_hao=xu_hao    ##杆件序号
        self.jie_dian=jie_dian##杆件节点
        self.E=E              ##弹性模量
        self.A=A              ##截面面积
        self.I=I              ##截面惯性矩
        self.i=E*I/L          ##杆件线刚度
        self.EA=E*A
        self.L=L              ##杆件长度
        self.a=a              ##杆件角度，顺时针为正
        self.lian_jie=lian_jie##杆件连接类型
        self.wei_yi_num=[[1,1,1,1],[1,1,1,1]]   ##杆端位移数
        for x in [0,1]:
            match self.lian_jie[x]:
                ##0为无新增，n为有n个新增位移，-n为有n个约束
                #[[x轴位移1,y轴位移1,转角1,标记是否计数1],[x轴位移2,y轴位移2,转角2，标记是否计数2]]
                ##连接，增加杆端，引入位移，所以新加
                case 0 :self.wei_yi_num[x]=[ 0, 0, 0, 0]  ##刚接
                case 1 :self.wei_yi_num[x]=[ 0, 0, 1, 0]  ##铰接
                case 2 :self.wei_yi_num[x]=[ 1, 0, 0, 0]  ##x轴向自由的定向连接
                case 3 :self.wei_yi_num[x]=[ 0, 1, 0, 0]  ##y轴向自由的定向连接
                case 4 :self.wei_yi_num[x]=[ 0, 0, 0, 0]  ##自由端
                ##支座,约束位移，所以扣除
                case 10:self.wei_yi_num[x]=[-1,-1,-1, 0]  ##固定支座
                case 11:self.wei_yi_num[x]=[-1,-1, 0, 0]  ##固定铰支座，弯矩自由
                case 12:self.wei_yi_num[x]=[ 0,-1,-1, 0]  ##定向支座，x轴自由
                case 13:self.wei_yi_num[x]=[-1, 0,-1, 0]  ##定向支座，y轴自由
                case 14:self.wei_yi_num[x]=[ 0, 0,-1, 0]  ##某某支座，限制弯矩
                case 15:self.wei_yi_num[x]=[-1, 0, 0, 0]  ##铰支座，限制x轴
                case 16:self.wei_yi_num[x]=[ 0,-1, 0, 0]  ##铰支座，限制y轴          
        print(self.wei_yi_num)
        if cos==0 and sin==0:
            self.cos=math.cos(a/180*math.pi)
            self.sin=math.sin(a/180*math.pi)
        elif round(cos*cos+sin*sin,1)==0.99:
            self.sin=sin          ##杆件角度正弦
            self.cos=cos          ##杆件角度余弦
        else :
            print('第%d号杆件输入有误，请检查角度输入！'%self.xu_hao)
             
    def T(self):##局部坐标系到整体坐标系的 坐标转换矩阵
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
        resault=self.T().T@self.jv_bu_zuo_biao_xi()@self.T()
        # print(self.jv_bu_zuo_biao_xi())
        return resault