import numpy as np
import math
import json

from force import force
from force_lib import force_lib
from gan_jian import gan_jian
from gan_jian_lib import gan_jian_lib
from application import application


####force类。转化函数中的杆件长度L
####force类，目前力的角度是整体坐标系下的角度，能否改成局部坐标系下的角度？？？？
#桁架

##结构位移表达向量，用作后处理用

##单位统一为：长度mm，力N，应力MPa，默认E=206000MPa ，角度默认 °（逆时针为正）。

##杆件索引使用杆件的编码不使用节点编码！！！
class config:
    def __init__(self):
        with open('config',mode='r',encoding='utf-8') as f:
            self.config=json.load(f)  
        self.gan_jian_E=self.config['gan_jian']['E']
        self.gan_jian_A=self.config['gan_jian']['A']
        self.gan_jian_I=self.config['gan_jian']['I']
        self.gan_jian_a=self.config['gan_jian']['a']
        self.gan_jian_L=self.config['gan_jian']['L']
        self.gan_jian_cos=self.config['gan_jian']['cos']
        self.gan_jian_sin=self.config['gan_jian']['sin']
        self.gan_jian_lian_jie=self.config['gan_jian']['lian_jie']
        self.force_a=self.config['force']['a']
        self.force_cos=self.config['force']['cos']
        self.force_sin=self.config['force']['sin']
        self.force_L=self.config['force']['L']
        self.force_duan_dian_jv=self.config['force']['duan_dian_jv']
        self.force_duan_dian_zhi=self.config['force']['duan_dian_zhi']


###一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一###  

###二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二###  

###三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三###

###四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四四###

###五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五五###            

###六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六六###    
def main():
    conf=config()
    app=application(config=conf)
    ganl=gan_jian_lib(config=conf)
    ganl.add(file=1)

    k=app.zheng_ti_jv_zhen(ganl) 
    print('原始整体刚度矩阵','\n',k)   

    forl=force_lib(config=conf)
    forl.add(file=1)

    f=app.hand_force(forl)
    print('原始f','\n',f)
    # f=np.array([[0,0,0,50000,30000,20000000,0,0,0]])
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    d31=np.array([[0,0,0,1,1,1,0,0,0,]])
    d35=np.array([[0,0,0,0,0,1,0,0,1,0,0,1]])
    d38=np.array([[0,0,0,1,1,1,1,1,1,0,0,0]])

    h=app.hou_chu_li(d31)
    hk=h[0]
    hf=h[1]

    print('后处理f','\n',hf)
    print('后处理k','\n',hk/100000)

    resault=app.ji_suan_wei_yi()
    print('结果\n',resault)

if __name__=='__main__':
    main()

