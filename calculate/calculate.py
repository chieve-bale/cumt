import numpy as np
import math
import json

####force类。转化函数中的杆件长度L
####force类，目前力的角度是整体坐标系下的角度，能否改成局部坐标系下的角度

##单位统一为：长度mm，力N，应力MPa，默认E=206000MPa ，角度默认 °（逆时针为正）。

##杆件索引使用杆件的编码不使用节点编码！！！
class config:
    def __init__(self):
        with open('config',mode='r',encoding='utf-8') as f:
            self.config=json.load(f)  
        print(self.config['gan_jian'])
        self.gan_jian_E=self.config['gan_jian']['E']
        self.gan_jian_A=self.config['gan_jian']['A']
        self.gan_jian_I=self.config['gan_jian']['I']
        self.gan_jian_a=self.config['gan_jian']['a']
        self.gan_jian_cos=self.config['gan_jian']['cos']
        self.gan_jian_sin=self.config['gan_jian']['sin']
        self.force_a=self.config['force']['a']
        self.force_cos=self.config['force']['cos']
        self.force_sin=self.config['force']['sin']



###一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一###  
class gan_jian:##定义杆件的原始单元刚度矩阵
    
    def __init__(self,xu_hao=0,jie_dian=[0,0],E=206000,A=1,I=1,L=1,a=0,cos=0,sin=0):##类初始化
        self.xu_hao=xu_hao    ##杆件序号
        self.jie_dian=jie_dian##杆件节点
        self.E=E              ##弹性模量
        self.A=A              ##截面面积
        self.I=I              ##截面惯性矩
        self.i=round(E*I/L,4)          ##杆件线刚度
        self.EA=round(E*A,4)
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
###二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二###  
class gan_jian_lib:##定义杆件库
    def __init__(self,config:dir):
        self.config=config
        self.table=[]
        self.gan_jian_num=0
        self.jie_dian_num=0
    def __add_hand(self):
        while True:
            can_shu={'xu_hao':0,'jie_dian':[0,0],'E':206000,'A':1,'I':1,'L':1,'a':0,'cos':0,'sin':0}
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
                self.gan_jian_num+=1
                self.jie_dian_num=max(can_shu['jie_dian'][0],can_shu['jie_dian'][1],self.jie_dian_num)
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

    def __add_auto(self):
        try:
            f=open('./gan_jian_lib.json',mode='r',encoding='utf-8')
        except:
            print('杆件库文件（gan_jian_lib.json）异常，请检查')
        else:
            can_shu_s=json.load(f)
            f.close()
            for can_shu in can_shu_s:
                self.gan_jian_num+=1
                self.jie_dian_num=max(can_shu['jie_dian'][0]+1,can_shu['jie_dian'][1]+1,self.jie_dian_num)
                self.table+=[gan_jian(xu_hao=can_shu['xu_hao'],\
                                    jie_dian=can_shu['jie_dian'],\
                                    E=can_shu.get('E',self.config.gan_jian_E),\
                                    A=can_shu.get('A',self.config.gan_jian_A),\
                                    I=can_shu.get('I',self.config.gan_jian_I),\
                                    L=can_shu['L'],\
                                    a=can_shu.get('a',self.config.gan_jian_a),\
                                    cos=can_shu.get('cos',self.config.gan_jian_cos),\
                                    sin=can_shu.get('sin',self.config.gan_jian_sin))]
   
    def add(self,file=0):##往杆件库中添加杆件，默认手动输入，file=1时读取json文件
        match file:
            case 0:
                self.__add_hand()
            case 1:
                self.__add_auto()
                
    def show(self):
        return self.table        
###三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三###
class force:
    def __init__(self,xu_hao=0,wei_zhi=[0],lei_xing='00',L=1,duan_dian=[0,0],duan_dian_zhi=[1,1],F=1,a=0,cos=0,sin=0,jie_gou=[]) -> None:
        self.xu_hao=xu_hao
        self.wei_zhi=wei_zhi
        self.lei_xing=lei_xing
        self.L=L
        self.duan_dian=duan_dian
        self.duan_dian_zhi=duan_dian_zhi
        self.F=F
        self.a=a
        self.cos=cos
        self.sin=sin
        self.jie_gou=jie_gou
        if self.cos==0 and self.sin==0:
            self.cos=round(math.cos(a/180*math.pi),3)
            self.sin=round(math.sin(a/180*math.pi),3)
        else:
            self.cos=cos
            self.sin=sin
        match self.lei_xing:
            case '00':self.force=np.array([[wei_zhi[0],self.F*self.cos,self.F*self.sin,0]])
            case '01':self.force=np.array([[self.wei_zhi[0],0,0,self.F]])
            case '10':self.force=self.pu_tong_deng_xiao('10')
            case '11':self.force=self.pu_tong_deng_xiao('11')
            case '3' :self.force=self.jun_bu_deng_xiao('3')
    def pu_tong_deng_xiao(self,code):
        a=self.duan_dian[0]
        b=self.duan_dian[1]
        L=self.L
        F=self.F
        s=self.sin
        c=self.cos
        match code:
            case '10':
                print(L)
                gu_duan=np.array([[self.wei_zhi[0],-(b*b*(L+2*a)*F*c/(L*L*L)),-(b*b*(L+2*a)*F*s/(L*L*L)), a*b*b*F/(L*L),\
                                   self.wei_zhi[0], (a*a*(L+2*b)*F*s/(L*L*L)), (a*a*(L+2*b)*F*s/(L*L*L)),-a*a*b*F/(L*L)]])
            # case '11':
            #     gu_duan=np.array([[]])
            case '11':
                gu_duan=np.array([[self.wei_zhi[0], 6*a*b*F*c/(L*L*L), 6*a*b*F*c/(L*L*L),-b*(3*a-L)*F/(L*L),\
                                   self.wei_zhi[0],-6*a*b*F*s/(L*L*L),-6*a*b*F*s/(L*L*L),-a*(3*b-L)*F/(L*L),]])
        return gu_duan
    def jun_bu_deng_xiao(self,code):
        match code:
            case '3':
                gu_duan=np.array([[]])
        return gu_duan
###四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四###
class force_lib:
    def __init__(self,config:dir) -> None:
        self.config=config
        self.table=[]
        self.force_num=0
        self.jie_dian_num=1
    def add(self,file=0):##往力库中添加力，默认手动输入，file=1时读取json文件
        match file:
            case 0:
                self.__add_hand()
            case 1:
                self.__add_auto()
    def __add_auto(self):
        try:
            f=open('./force.json',mode='r',encoding='utf-8')
        except:
            print('力库文件（force.json）异常，请检查')
        else:
            can_shu_s=json.load(f)
            f.close()
            for can_shu in can_shu_s:
                self.table+=[force(xu_hao=can_shu['xu_hao'],\
                                wei_zhi=can_shu['wei_zhi'],\
                                lei_xing=can_shu['lei_xing'],\
                                L=can_shu['L'],\
                                duan_dian=can_shu['duan_dian'],\
                                duan_dian_zhi=can_shu['duan_dian_zhi'],\
                                F=can_shu['F'],\
                                a=can_shu.get('a',self.config.force_a),\
                                cos=can_shu.get('cos',self.config.force_cos),\
                                sin=can_shu.get('sin',self.config.force_sin))]
    def __add_hand(self):
        while True:
            can_shu={'xu_hao':0,'wei_zhi':[0,0],'lei_xing':'00','chang_du':1,'duan_dian':[10,10],'duan_dian_zhi':[1,1],'F':1,'a':0,'cos':0,'sin':0}
            can_shu=input("按照字典输入杆件参数{'xu_hao':0,'wei_zhi':[0,0],'lei_xing':'00','chang_du':1,\
                          'duan_dian':[10,10],'duan_dian_zhi':[1,1],'F':1,'a':0,'cos':0,'sin':0}（q退出输入）：")
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
                self.table+=[force(xu_hao=can_shu['xu_hao'],\
                                   wei_zhi=can_shu['wei_zhi'],\
                                   lei_xing=can_shu['lei_xing'],\
                                   chang_du=can_shu['chang_du'],\
                                   duan_dian=can_shu['duan_dian'],\
                                   duan_dian_zhi=can_shu['duan_dian_zhi'],\
                                   F=can_shu['F'],\
                                   a=can_shu.get('a',self.config.force_a),\
                                   cos=can_shu.get('cos',self.config.force_cos),\
                                   sin=can_shu.get('sin',self.config.force_sin))]
                self.jie_dian_num+=1
            else:
                print("输入有误，请重新输入")  
    def show(self):
        print(self.table)
        return self.table
###五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五###            
class application:
    def __init__(self,config:dir):##结果初始化
        self.config=config
        self.jv_zhen=np.array([[]])
        self.wei_yi_xiang_liang =np.array([[]])
        self.force_xiang_liang  =np.array([[]])
    def zheng_ti_jv_zhen(self,gan_jian_lib):##输入节点数和杆件数
        jie_dian_num=gan_jian_lib.jie_dian_num
        jv_zhen=np.zeros((jie_dian_num*3,jie_dian_num*3))##创建初始 结构原始刚度矩阵
        ###这段代码繁杂但nb，可以实现杆端编号不连续（例如五号杆件两端节点为3，9），或者两个节点中间有n多个杆
        for i in gan_jian_lib.table:#i是每个杆件的实例'
            print(i.zheng_ti_zuo_biao_xi())
    ##        print(i.jie_dian)
            for x in range(3):
                for y in range(3):                
                    jv_zhen[i.jie_dian[0]*3+x,i.jie_dian[0]*3+y]=jv_zhen[i.jie_dian[0]*3+x,i.jie_dian[0]*3+y]\
                        +round(i.zheng_ti_zuo_biao_xi()[x,y],3)
    ##                print(i.jie_dian[0]*3+x,i.jie_dian[0]*3+y,x,y)
            for x in range(3):
                for y in range(3):
                    jv_zhen[i.jie_dian[0]*3+x,i.jie_dian[1]*3+y]=jv_zhen[i.jie_dian[0]*3+x,i.jie_dian[1]*3+y]\
                        +round(i.zheng_ti_zuo_biao_xi()[x,y+3],3)
    ##                print(i.jie_dian[0]*3+x,i.jie_dian[1]*3+y,x,y+3)
            for x in range(3):
                for y in range(3):                
                    jv_zhen[i.jie_dian[1]*3+x,i.jie_dian[0]*3+y]=jv_zhen[i.jie_dian[1]*3+x,i.jie_dian[0]*3+y]\
                        +round(i.zheng_ti_zuo_biao_xi()[x+3,y],3)
    ##                print(i.jie_dian[1]*3+x,i.jie_dian[0]*3+y,x+3,y)
            for x in range(3):
                for y in range(3):                
                    jv_zhen[i.jie_dian[1]*3+x,i.jie_dian[1]*3+y]=jv_zhen[i.jie_dian[1]*3+x,i.jie_dian[1]*3+y]\
                        +round(i.zheng_ti_zuo_biao_xi()[x+3,y+3])
    ##                print(i.jie_dian[1]*3+x,i.jie_dian[1]*3+y,x+3,y+3)
    ##        print(i.zheng_ti_zuo_biao_xi())
        self.jv_zhen=jv_zhen     
        return jv_zhen##原始刚度矩阵
    def hand_force(self,force_lib):
        table=force_lib.table
        jie_dian_num=3#force_lib.jie_dian_num
        force_xiang_liang=np.zeros((jie_dian_num*3))
        for i in force_lib.table:#i是每个力的实例
            for x in range(3):
                if len(i.force)==1:#每个力有两个位置参数
                    force_xiang_liang[i.wei_zhi[0]*3+x]=force_xiang_liang[i.wei_zhi[0]*3+x]+round(i.force[0,x+1],3)
                elif len(i.force)==2:
                    force_xiang_liang[i.wei_zhi[0]*3+x]=force_xiang_liang[i.wei_zhi[0]*3+x]+round(i.force[0,x+1],3)
                    force_xiang_liang[i.wei_zhi[1]*3+x]=force_xiang_liang[i.wei_zhi[1]*3+x]+round(i.force[1,x+1],3)
        self.force_xiang_liang=force_xiang_liang
        return force_xiang_liang

    def hou_chu_li(self,jv_zhen,force,wei_yi) -> list:
        rows_to_delete=[]
        cols_to_delete=[]
        lens=len(wei_yi[0])
        for x in range(lens):
            if wei_yi[0][x]==0:
                rows_to_delete+=[x]
        for y in range(lens):
            if wei_yi[0][y]==0:
                cols_to_delete+=[y]
    ##    print(rows_to_delete)
    ##    print(cols_to_delete)
        ##删除多余的行和列
        jv_zhen=np.delete(jv_zhen,rows_to_delete,axis=0)
    ##    print(jv_zhen)
        jv_zhen=np.delete(jv_zhen,cols_to_delete,axis=1)
    ##    print(jv_zhen)
        force=np.delete(force,cols_to_delete,axis=0)
        return [jv_zhen,force]
    def ji_suan_wei_yi(self,jv_zhen,force):
        k_ni=np.linalg.inv(jv_zhen)##求k的逆
        wei_yi=k_ni@force
        self.wei_yi_xiang_liang=wei_yi
        return wei_yi
###六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六###    
def main():
    conf=config()
    app=application(config=conf)
    ganl=gan_jian_lib(config=conf)
    ganl.add(file=1)

    k=app.zheng_ti_jv_zhen(ganl) 
    print(k)   

    forl=force_lib(config=conf)
    forl.add(file=1)


    f=app.hand_force(forl)
    # f=np.array([[0,0,0,50000,30000,20000000,0,0,0]])
    print('&&&&&&&&')
    d=np.array([[0,0,0,1,1,1,0,0,0]])

    h=app.hou_chu_li(k,f,d)
    k=h[0]
    f=h[1]

    print(f)

    resault=app.ji_suan_wei_yi(k,f.T)
    print(resault)

if __name__=='__main__':
    main()

