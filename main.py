from calculate import *

def main():
    gan_jian_lib=gan_jian_lib()
    gan_jian_lib.add(file=1)
    gan_jian_lib.show()
    a=gan_jian_jv_zhen(jie_dian_shu=3,gan_jian_shu=2,gan_jian_lib=gan_jian_lib)
    print(a)
if __name__ == 'main' :
    main()
