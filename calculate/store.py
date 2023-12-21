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