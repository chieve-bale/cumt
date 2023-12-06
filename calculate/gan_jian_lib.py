import numpy as np
import math
import json

from gan_jian import gan_jian

class gan_jian_lib:##定义杆件库
    def __init__(self,config:dir):
        self.config=config
        self.table=[]
        self.gan_jian_num=0
        self.jie_dian_num=0
        self.wei_yi_num=0
        self.wei_yi_mu_ban=np.array([])
    def add(self,file=0):##往杆件库中添加杆件，默认手动输入，file=1时读取json文件
        match file:
            case 0:self.__add_hand()
            case 1:self.__add_auto()
    def __add_auto(self):
        try:
            f=open('./gan_jian_lib.json',mode='r',encoding='utf-8')
        except:
            print('杆件库文件（gan_jian_lib.json）异常，请检查')
        else:
            can_shu_s=json.load(f)
            f.close()
            for can_shu in can_shu_s:
                ##统计杆件数
                self.gan_jian_num+=1
                ##统计节点数
                self.jie_dian_num=max(self.jie_dian_num,max(can_shu.get('jie_dian',[0,0]))+1)
                ##生成杆件对象的列表
                self.table+=[gan_jian(xu_hao=can_shu['xu_hao'],\
                                    jie_dian=can_shu['jie_dian'],\
                                    E=can_shu.get('E',self.config.gan_jian_E),\
                                    A=can_shu.get('A',self.config.gan_jian_A),\
                                    I=can_shu.get('I',self.config.gan_jian_I),\
                                    L=can_shu.get('L',self.config.gan_jian_L),\
                                    a=can_shu.get('a',self.config.gan_jian_a),\
                                    cos=can_shu.get('cos',self.config.gan_jian_cos),\
                                    sin=can_shu.get('sin',self.config.gan_jian_sin),\
                                    lian_jie=can_shu.get('lian_jie',self.config.gan_jian_lian_jie))]
                
    def tong_ji(self):##1,单独输入对节点的定义，2,遍历每个杆件，并记录已统计的节点，3,遍历每个杆件，另寻他法！！！！
        self.wei_yi_mu_ban=[]#位移模板
        for j_d in range(self.jie_dian_num):###统计
            ##杆端位移数,不存在为0，独立（连接两边位移不相等，即变形不连续）为1，非独立（连接两边位移相等，即变形连续）为2
            #[[x轴位移1,y轴位移1,转角1,标记是否计数1],[x轴位移2,y轴位移2,转角2，标记是否计数2]]
            for gan in self.table:
                if gan.jie_dian[0]==j_d:
                    self.wei_yi_mu_ban+=[[x+y for x, y in zip([1,1,1],gan.wei_yi_num[0][0:3])]]##处理位移模板
                    gan.wei_yi_num[0][3]+=1##标记为已计数
                if gan.jie_dian[1]==j_d:
                    self.wei_yi_mu_ban+=[[x+y for x, y in zip([1,1,1],gan.wei_yi_num[1][0:3])]]##处理位移模板
                    gan.wei_yi_num[1][3]+=1##标记为已计数
                print(self.wei_yi_mu_ban)                    
        self.wei_yi_num=np.sum(np.array(self.wei_yi_mu_ban))

             
    def show(self):
        return self.table
    
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