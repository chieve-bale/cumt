import numpy as np
import math
import json

from he_zai import he_zai
from he_zai_lib import he_zai_lib
from gan_jian import gan_jian
from gan_jian_lib import gan_jian_lib

class application:
    def __init__(self,config:dir):##结果初始化
        self.config=config
        self.jv_zhen=np.array([[]])
        self.wei_yi_xiang_liang =np.array([[]])
        self.he_zai_xiang_liang  =np.array([[]])
        self.jie_dian_num:int
        self.wei_yi_num:int
    def zheng_ti_jv_zhen(self,gan_jian_lib):##输入节点数和杆件数
        self.wei_yi_num=gan_jian_lib.wei_yi_num
        self.jv_zhen=np.zeros((self.wei_yi_num,self.wei_yi_num))##创建初始 结构原始刚度矩阵
        for gan in gan_jian_lib.table:
            for x in zip(gan.ding_wei,list(range(6))):
                for y in zip(gan.ding_wei,list(range(6))):
                    self.jv_zhen[x[0]][y[0]]+=gan.zheng_ti_zuo_biao_xi[x[1]][y[1]]
        return self.jv_zhen##原始刚度矩阵
    
    def hand_he_zai(self,he_zai_lib):
        he_zai_xiang_liang=np.zeros((self.wei_yi_num))
        for he_zai in he_zai_lib.table:#i是每个力的实例
            pass
        return he_zai_xiang_liang

    def hou_chu_li(self,wei_yi) -> list:
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
        self.jv_zhen=np.delete(self.jv_zhen,rows_to_delete,axis=0)
    ##    print(jv_zhen)
        self.jv_zhen=np.delete(self.jv_zhen,cols_to_delete,axis=1)
    ##    print(jv_zhen)
        self.he_zai_xiang_liang=np.delete(self.he_zai_xiang_liang,cols_to_delete,axis=0)
        return [self.jv_zhen,self.he_zai_xiang_liang]
    
    def ji_suan_wei_yi(self):
        k_ni=np.linalg.inv(self.jv_zhen)##求k的逆
        self.wei_yi_xiang_liang=k_ni@self.he_zai_xiang_liang
        return self.wei_yi_xiang_liang