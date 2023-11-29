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
            case 0:
                self.__add_hand()
            case 1:
                self.__add_auto()
    def __add_hand(self):
        pass
    def __add_auto(self):
        try:
            f=open('./force.json',mode='r',encoding='utf-8')
        except:
            print('力库文件（force.json）异常，请检查')
        else:
            can_shu_s=json.load(f)
            f.close()
            for can_shu in can_shu_s:
                ff=force(xu_hao=can_shu['xu_hao'],\
                                wei_zhi=can_shu['wei_zhi'],\
                                lei_xing=can_shu['lei_xing'],\
                                L=can_shu.get('L',self.config.force_L),\
                                duan_dian=can_shu.get('duan_dian',self.config.force_duan_dian),\
                                duan_dian_zhi=can_shu.get('duan_dian_zhi',self.config.force_duan_dian_zhi),\
                                F=can_shu['F'],\
                                a=can_shu.get('a',self.config.force_a),\
                                cos=can_shu.get('cos',self.config.force_cos),\
                                sin=can_shu.get('sin',self.config.force_sin))
                self.table+=[ff]
                self.force_num+=1

    def show(self):
        print(self.table)
        return self.table