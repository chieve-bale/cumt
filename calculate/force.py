import numpy as np
import math
import json

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
            case '00':self.force=np.array([[self.F*self.cos,self.F*self.sin,0     ]])
            case '01':self.force=np.array([[0              ,0              ,self.F]])
            case '10':self.force=self.pu_tong_deng_xiao('10')
            case '11':self.force=self.pu_tong_deng_xiao('11')
            case '3' :self.force=self.jun_bu_deng_xiao('3')
    def pu_tong_deng_xiao(self,code):
        a=self.duan_dian[0]
        b=self.duan_dian[1]
        L=a+b
        F=self.F
        s=self.sin
        c=self.cos
        match code:
            case '10':
                gan_duan=np.array([[  (b*b*(L+2*a)*F*c/(L*L*L)),(b*b*(L+2*a)*F*s/(L*L*L)), a*b*b*F/(L*L)],\
                                    [(a*a*(L+2*b)*F*s/(L*L*L)),(a*a*(L+2*b)*F*s/(L*L*L)),-a*a*b*F/(L*L)]])
            case '11':
                gan_duan=np.array([[   6*a*b*F*c/(L*L*L), 6*a*b*F*c/(L*L*L),-b*(3*a-L)*F/(L*L)],\
                                    [-6*a*b*F*s/(L*L*L),-6*a*b*F*s/(L*L*L), a*(3*b-L)*F/(L*L),]])
        return gan_duan
    def jun_bu_deng_xiao(self,code):
        ##有待完善通用情况下的计算
        F=self.F
        L=self.L
        duan_dian=self.duan_dian
        duan_dian=self.duan_dian_zhi
        match code:
            case '3':
                gan_duan=np.array([[0,F*L/2, F*L*L/12],\
                                   [0,F*L/2,-F*L*L/12]])
        return gan_duan