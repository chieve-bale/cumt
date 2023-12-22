import numpy as np
import math
import json
##完成定位向量
from gan_jian import gan_jian

class gan_jian_lib:##定义杆件库
    def __init__(self,config:dir):
        self.config=config##导入设置
        self.table=[]##初始杆件列表
        self.gan_jian_num=0##杆件数
        self.jie_dian_num=0##节点数
        self.wei_yi_num=0##位移数，包含支座的零位移
        self.wei_yi_mu_ban=[]#位移模板
    def add(self,file=0):##往杆件库中添加杆件，默认手动输入，file=1时读取json文件
        match file:
            case 0:self.__add_hand()
            case 1:self.__add_auto()
    def __add_auto(self):
        try:
            f=open('./can_shu.json',mode='r',encoding='utf-8')
        except:
            print('杆件库文件（can_shu.json）杆件部分异常，请检查')
        else:
            can_shu_s=json.load(f)['gan_jian']
            f.close()
            print(type(can_shu_s))
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
        ##统计位移模板########################################################################
        for j_d in range(self.jie_dian_num):###统计节点位移模板
            ##杆端位移数,不存在为0，独立（连接两边位移不相等，即变形不连续）为1，非独立（连接两边位移相等，即变形连续）为2
            #[[x轴位移1,y轴位移1,转角1,标记是否计数1],[x轴位移2,y轴位移2,转角2，标记是否计数2]]
            jie_dian_wei_yi_num=[1,1,1]
            for gan in self.table:
                if gan.jie_dian[0]==j_d:
                    jie_dian_wei_yi_num=[x+y for x, y in zip(jie_dian_wei_yi_num,gan.wei_yi_num[0][0:3])]##处理位移模板
                    gan.wei_yi_num[0][3]+=1##标记为已计数
                if gan.jie_dian[1]==j_d:                
                    jie_dian_wei_yi_num=[x+y for x, y in zip(jie_dian_wei_yi_num,gan.wei_yi_num[1][0:3])]##处理位移模板
                    gan.wei_yi_num[1][3]+=1##标记为已计数
            jie_dian_wei_yi_num=[i-1 if i>1 else i for i in jie_dian_wei_yi_num]##
            self.wei_yi_mu_ban+=[jie_dian_wei_yi_num]##组合 
        ##统计位移数，处理位移向量模板##############################################################
        self.wei_yi_xiang_liang_mu_ban=[]
        for i in range(self.jie_dian_num):##
            self.wei_yi_xiang_liang_mu_ban.append([])
            for j in range(3):
                match self.wei_yi_mu_ban[i][j]:
                    case 0:self.wei_yi_num+=1;self.wei_yi_xiang_liang_mu_ban[i]+=[0]
                    case x if x>=1:self.wei_yi_num+=x;self.wei_yi_xiang_liang_mu_ban[i]+=[1]*x
        # print('杆件数',self.gan_jian_num)
        # print('节点数',self.jie_dian_num)
        # print('位移数',self.wei_yi_num)
        # print('位移模板',self.wei_yi_mu_ban)
        # print('位移向量模板',self.wei_yi_xiang_liang_mu_ban)
        ##处理定位向量#########################################################################
        ##按节点生成
        '''
        杆的一端的定位向量表达式:i、j、k为新增多余位移个数
        [3*j_d+0+i,3*j_d+1+j,3*j_d+2+k]
        '''
        lei_ji=0
        for jd in range(self.jie_dian_num):
            x,y,z=[0,0,0]
            for gan in self.table:
                if gan.jie_dian[0]==jd:
                    i=1 if gan.wei_yi_num[0][0] == 1 else 0
                    j=1 if gan.wei_yi_num[0][1] == 1 else 0
                    k=1 if gan.wei_yi_num[0][2] == 1 else 0
                    x,y,z=[x+i,y+j,z+k]
                    gan.ding_wei[0:3]=[gan.jie_dian[0]*3+0+x+lei_ji,\
                                       gan.jie_dian[0]*3+1+y+lei_ji,\
                                       gan.jie_dian[0]*3+2+z+lei_ji]                                       
                if gan.jie_dian[1]==jd:
                    i=1 if gan.wei_yi_num[1][0] == 1 else 0
                    j=1 if gan.wei_yi_num[1][1] == 1 else 0
                    k=1 if gan.wei_yi_num[1][2] == 1 else 0
                    gan.ding_wei[3:6]=[gan.jie_dian[1]*3+0+x+lei_ji,\
                                       gan.jie_dian[1]*3+1+y+lei_ji,\
                                       gan.jie_dian[1]*3+2+z+lei_ji]
            lei_ji+=len(self.wei_yi_xiang_liang_mu_ban[jd])-3##此节点前的节点，累计多余位移个数
        
        for gan in self.table:
            print(gan.xu_hao,'杆的定位',gan.ding_wei)
        

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