import numpy as np
import math
import json
##单位统一为：长度mm，力N，应力MPa，默认E=206000MPa ，角度默认 °（逆时针为正）

##杆件索引使用杆件的编码不使用节点编码！！！

   
class gan_jian:##定义杆件的原始单元刚度矩阵
    
    def __init__(self,xu_hao=0,jie_dian=(0,0),E=206000,A=1,I=1,L=1,a=0,cos=0,sin=0):##类初始化
        self.xu_hao=xu_hao    ##杆件序号
        self.jie_dian=jie_dian##杆件节点
        self.E=E              ##弹性模量
        self.A=A              ##截面面积
        self.I=I              ##截面惯性矩
        self.i=E*A/L          ##杆件线刚度
        self.L=L              ##杆件长度
        self.a=a              ##杆件角度，顺时针为正
        self.sin=sin          ##杆件角度正弦
        self.cos=cos          ##杆件角度余弦
              
    def TT(self):##局部坐标系到整体坐标系的 坐标转换矩阵
        if self.cos==0 and self.sin==0:##输入杆件三角函数
            a=(self.a/180)*math.pi
            return np.array([[ math.cos(a) ,math.sin(a)  ,0       ,0             ,0            ,0],\
                             [-math.sin(a) ,math.cos(a)  ,0       ,0             ,0            ,0],\
                             [0            ,0            ,1       ,0             ,0            ,0],\
                             [0            ,0            ,0       , math.cos(a)  ,math.sin(a)  ,0],\
                             [0            ,0            ,0       ,-math.sin(a)  ,math.cos(a)  ,0],\
                             [0            ,0            ,0       ,0             ,0            ,1]])
        else:##输入杆件角度
            s=self.sin
            c=self.cos
            s=-0.894
            c=0.447   
            return np.array([[c,s,0,0,0,0],\
                             [-s,c,0,0,0,0],\
                             [0,0,1,0,0,0],\
                             [0,0,0,c,s,0],\
                             [0,0,0,-s,c,0],\
                             [0,0,0,0,0,1]])
        
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

#######################################################################################################################################################################    

class gan_jian_lib:##定义杆件库
    def __init__(self):
        self.table=[]
   
    def add(self,file=0):##往杆件库中添加杆件，默认手动输入，file=1时读取json文件
        match file:
            case 0:
                add_hand()
            case 1:
                add_auto()

    def add_hand(self):
        while True:
            can_shu={'xu_hao':0,'jie_dian':(0,0),'E':206000,'A':1,'I':1,'L':1,'a':0,'cos':0,'sin':0}
            can_shu=input("按照字典输入杆件参数{'xu_hao':0,'jie_dian':(0,0),'E':206000,'A':1,'I':1,'L':1,'a':0,'cos':0,'sin':0}（q退出输入）：")
            len_can_shu=len(can_shu)
            if can_shu=='q':
                break
            elif can_shu=='show':
                print(self.table)
            elif can_shu=='ok':
                print(self.table)
                return self.table
                break
            elif len(can_shu) > 5:
                can_shu=eval(can_shu)
                self.table+=[gan_jian(xu_hao=can_shu['xu_hao'],\
                             jie_dian=can_shu['jie_dian'],\
                             E=can_shu['E'],\
                             A=can_shu['A'],\
                             I=can_shu['I'],\
                             L=can_shu['L'],\
                             a=can_shu['a'],\
                             cos=can_shu['cos'],\
                             sin=can_shu['sin'])]
            else:
                print("输入有误，请重新输入")  

    def add_auto():
        try:
            f=open('./gan_jian_lib.json', mode='r',encoding='utf-8')
        except:
            print('杆件库文件（gan_jian_lib.json）异常，请检查')
        else:
            json.load(f,ensure_ascii=False, encoding='utf-8')
    def show(self):
        print(self.table)
        return self.table


    
##a=np.array([[168,0,0,-168,0,0],[0,8.064,20.16,0,-8.064,20.16],[0,20.16,67.2,0,-20.16,33.6],[-168,0,0,168,0,0],[0,-8.064,-20.16,0,8.064,-20.16],[0,20.16,33.6,0,-20.16,67.2]])
##b=np.array([[150.3,0,0,-150.3,0,0],[0,5.771,16.13,0,-5.771,16.13],[0,16.13,60.1,0,-16.13,30.1],[-150.3,0,0,150.3,0,0],[0,-5.771,-16.13,0,5.771,-16.13],[0,16.13,30.1,0,-16.13,60.1]])
##c=gan_jian().TT().T@b@gan_jian().TT()

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

##print(gan_jian_jv_zhen(3,2,gan_jian_list))

def hou_chu_li(jv_zhen):
    pass
    
gan_jian_lib().add()










##############################################################################################################
def main():
##    {'I':40000000000,'A':400000,'E':210000,'L':5590,'xu_hao':1,'a':0}
##    gj=gan_jian(I=40000000000,A=400000,E=210000,L=5590,xu_hao=1,a=0)
##    t=gj.TT()
##    k=gj.jv_bu_zuo_biao_xi()
##    print(t.T,k,t)
##    print(t.T@k@t)
    pass

if __name__=='__main__':
    main()




##a=np.array([[150.3,0,0,-150.3,0,0],[0,5.771,16.13,0,-5.771,16.13],[0,16.13,60.1,0,-16.13,30.1],[-150.3,0,0,150.3,0,0],[0,-5.771,-16.13,0,5.771,-16.13],[0,16.13,30.1,0,-16.13,60.1]])

##aa=np.zeros((3,3))
