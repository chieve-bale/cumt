import numpy as np
import math

##需要对均布力积分求杆端等效节点荷载
class he_zai:
    def __init__(self,xu_hao=0,wei_zhi=[0],lei_xing='00',L=1,duan_dian_jv=[0,0],duan_dian_zhi=[1,1],F=1,a=0,cos=0,sin=0) -> None:
        self.xu_hao=xu_hao
        self.wei_zhi=wei_zhi
        self.lei_xing=lei_xing
        self.L=L
        self.duan_dian_jv=duan_dian_jv
        self.duan_dian_zhi=duan_dian_zhi
        self.F=F
        self.a=a
        if cos==0 and sin==0:
            self.cos=round(math.cos(a/180*math.pi),3)
            self.sin=round(math.sin(a/180*math.pi),3)
        elif round(cos*cos+sin*sin,1)==1:
            self.sin=sin          ##杆件角度正弦
            self.cos=cos          ##杆件角度余弦
        else :
            print('第%d号力输入有误，请检查角度输入！'%self.xu_hao)

        match self.lei_xing:
            case '00':self.he_zai=np.array([[self.F*self.cos,self.F*self.sin,0     ]])
            case '01':self.he_zai=np.array([[0              ,0              ,self.F]])
            case '10':self.he_zai=self.pu_tong_deng_xiao('10')
            case '11':self.he_zai=self.pu_tong_deng_xiao('11')
            case '3' :self.he_zai=self.jun_bu_deng_xiao('3')
    def pu_tong_deng_xiao(self,code):
        a=self.duan_dian_jv[0]
        b=self.duan_dian_jv[1]
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
        a=self.duan_dian_jv[0]
        b=self.duan_dian_jv[1]
        q1=self.duan_dian_zhi[0]
        q2=self.duan_dian_zhi[1]
        match code:
            case '3':
                gan_duan=np.array([[0,F*L/2, F*L*L/12],\
                                   [0,F*L/2,-F*L*L/12]])
        return gan_duan