import numpy as np
import math
import json

from force import force

class force_lib:
    def __init__(self,config:dir) -> None:
        self.config=config
        self.table=[]
        self.force_num=0
    def add(self,file=0):##往力库中添加力，默认手动输入，file=1时读取json文件
        match file:
            case 0:self.__add_hand()
            case 1:self.__add_auto()
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
                        L=can_shu.get('L',self.config.force_L),\
                        duan_dian=can_shu.get('duan_dian',self.config.force_duan_dian),\
                        duan_dian_zhi=can_shu.get('duan_dian_zhi',self.config.force_duan_dian_zhi),\
                        F=can_shu['F'],\
                        a=can_shu.get('a',self.config.force_a),\
                        cos=can_shu.get('cos',self.config.force_cos),\
                        sin=can_shu.get('sin',self.config.force_sin))]
                self.force_num+=1

    def show(self):
        print(self.table)
        return self.table
    
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
