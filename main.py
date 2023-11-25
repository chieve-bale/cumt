import calculate
import numpy as np

def main():
    gan_jian_lib=calculate.gan_jian_lib()
    gan_jian_lib.add(file=1)
    k=calculate.gan_jian_jv_zhen(jie_dian_shu=3,gan_jian_shu=2,gan_jian_lib=gan_jian_lib.table)
    
    f=np.array([[0,0,0,50000,30000,20000000,0,0,0]])##力
    d=np.array([[0,0,0,1,1,1,0,0,0]])##假的位移，用来后处理的
    
    h=calculate.hou_chu_li(k,f,d)
    
    resault=calculate.ji_suan_wei_yi(h[0],h[1].T)
    print(resault)
    
if __name__ == '__main__':
    main()
