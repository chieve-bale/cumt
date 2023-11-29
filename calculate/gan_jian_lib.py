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
    def __add_hand(self):
        pass
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
                self.jie_dian_num=max(self.jie_dian_num,max(can_shu.get('jie_dian',[0,0]))+1)
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