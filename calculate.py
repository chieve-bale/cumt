import numpy as np
from math import cos,sin,pi
##单位统一为：长度mm，力N，应力MPa，默认E=206000MPa ，角度默认 °（逆时针为正）

##杆件索引使用杆件的编码不使用节点编码！！！


class gan_jian:##定义杆件的原始单元刚度矩阵
    
    def __init__(self,xu_hao=0,jie_dian=(0,0),E=206000,A=1,I=1,L=1,a=0):##类初始化
        self.xu_hao=xu_hao
        self.jie_dian=jie_dian
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
a=np.array([[168,0,0,-168,0,0],[0,8.064,20.16,0,-8.064,20.16],[0,20.16,67.2,0,-20.16,33.6],[-168,0,0,168,0,0],[0,-8.064,-20.16,0,8.064,-20.16],[0,20.16,33.6,0,-20.16,67.2]])
b=np.array([[150.3,0,0,-150.3,0,0],[0,5.771,16.13,0,-5.771,16.13],[0,16.13,60.1,0,-16.13,30.1],[-150.3,0,0,150.3,0,0],[0,-5.771,-16.13,0,5.771,-16.13],[0,16.13,30.1,0,-16.13,60.1]])
c=gan_jian().TT().T@b@gan_jian().TT()

def gan_jian_list(gan_jian_shu,jie_dian):
    for i in range(gan_jian_shu):
        ll=[]
        l=gan_jian(xu_hao=i,jie_dian=jie_dian,)
        
    return[{'gan_jian_xu_hao':0,'jie_dian':(0,1),'c':a},{'gan_jian_xu_hao':1,'jie_dian':(1,2),'c':c}]

def gan_jian_jv_zhen(jie_dian_shu,gan_jian_shu,gan_jian_list):##输入节点数和杆件数
    jv_zhen=np.zeros((jie_dian_shu*3,jie_dian_shu*3))##创建初始 结构原始刚度矩阵


    for i in gan_jian_list:###这段代码繁杂但nb，可以实现杆端编号不连续（例如五号杆件两端节点为3，9），或者两个节点中间有n多个杆
        for x in range(3):
            for y in range(3):                
                jv_zhen[i['jie_dian'][0]*3+x,i['jie_dian'][0]*3+y]=jv_zhen[i['jie_dian'][0]*3+x,i['jie_dian'][0]*3+y]+i['c'][x,y]
        for x in range(3):
            for y in range(3):
                jv_zhen[i['jie_dian'][0]*3+x,i['jie_dian'][1]*3+y]=jv_zhen[i['jie_dian'][0]*3+x,i['jie_dian'][1]*3+y]+i['c'][x,y+3]
        for x in range(3):
            for y in range(3):                
                jv_zhen[i['jie_dian'][1]*3+x,i['jie_dian'][0]*3+y]=jv_zhen[i['jie_dian'][1]*3+x,i['jie_dian'][0]*3+y]+i['c'][x+3,y]
        for x in range(3):
            for y in range(3):                
                jv_zhen[i['jie_dian'][1]*3+x,i['jie_dian'][1]*3+y]=jv_zhen[i['jie_dian'][1]*3+x,i['jie_dian'][1]*3+y]+i['c'][x+3,y+3]



    return jv_zhen##原始刚度矩阵

print(gan_jian_jv_zhen(3,2,gan_jian_list))

def hou_chu_li(jv_zhen):
    pass
    
    
def main():
    pass

if __name__=='__main__':
    main




##a=np.array([[150.3,0,0,-150.3,0,0],[0,5.771,16.13,0,-5.771,16.13],[0,16.13,60.1,0,-16.13,30.1],[-150.3,0,0,150.3,0,0],[0,-5.771,-16.13,0,5.771,-16.13],[0,16.13,30.1,0,-16.13,60.1]])

##aa=np.zeros((3,3))
