import numpy as np
import math
import json

from force import force
from force_lib import force_lib
from gan_jian import gan_jian
from gan_jian_lib import gan_jian_lib

class application:
    def __init__(self,config:dir):##结果初始化
        self.config=config
        self.jv_zhen=np.array([[]])
        self.wei_yi_xiang_liang =np.array([[]])
        self.force_xiang_liang  =np.array([[]])
        self.jie_dian_num:int
        self.wei_yi_num:int
    def zheng_ti_jv_zhen(self,gan_jian_lib):##输入节点数和杆件数
        self.jie_dian_num=gan_jian_lib.jie_dian_num
        self.wei_yi_num=gan_jian_lib.wei_yi_num
        jv_zhen=np.zeros((self.wei_yi_num,self.wei_yi_num))##创建初始 结构原始刚度矩阵
        ###这段代码繁杂但nb，可以实现杆端编号不连续（例如五号杆件两端节点为3，9），或者两个节点中间有n多个杆

        for i in gan_jian_lib.table:#i是每个杆件的实例'
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
        force_xiang_liang=np.zeros((self.jie_dian_num*3))
        for i in force_lib.table:#i是每个力的实例
            print('序号',i.xu_hao,i.force)
            print(i.wei_zhi[0],i.wei_zhi[1])
            print("加入前",force_xiang_liang)
            for x in range(3):
                if len(i.force)==1:#每个力有两个位置参数
                    ##i.force[0,x] 索引第0行第x列的值
                    # print(i.force[0,x])
                    # print('+',force_xiang_liang[i.wei_zhi[0]*3+x],i.wei_zhi[0]*3+x)
                    force_xiang_liang[i.wei_zhi[0]*3+x]=force_xiang_liang[i.wei_zhi[0]*3+x]+i.force[0,x]
                    # print('=',force_xiang_liang[i.wei_zhi[0]*3+x])
                elif len(i.force)==2:
                    # print(i.force[0,x])
                    # print('+',force_xiang_liang[i.wei_zhi[0]*3+x],i.wei_zhi[0]*3+x)
                    force_xiang_liang[i.wei_zhi[0]*3+x]=force_xiang_liang[i.wei_zhi[0]*3+x]+i.force[0,x]
                    # print('=',force_xiang_liang[i.wei_zhi[0]*3+x])

                    # print(i.force[1,x])
                    # print('+',force_xiang_liang[i.wei_zhi[1]*3+x],i.wei_zhi[1]*3+x)
                    force_xiang_liang[i.wei_zhi[1]*3+x]=force_xiang_liang[i.wei_zhi[1]*3+x]+i.force[1,x]
                    # print('=',force_xiang_liang[i.wei_zhi[1]*3+x])
            print('f加完后',force_xiang_liang)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            # print(i.xu_hao,'完成',force_xiang_liang)
        self.force_xiang_liang=force_xiang_liang
        return force_xiang_liang

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
        self.force_xiang_liang=np.delete(self.force_xiang_liang,cols_to_delete,axis=0)
        return [self.jv_zhen,self.force_xiang_liang]
    
    def ji_suan_wei_yi(self):
        k_ni=np.linalg.inv(self.jv_zhen)##求k的逆
        self.wei_yi_xiang_liang=k_ni@self.force_xiang_liang
        return self.wei_yi_xiang_liang