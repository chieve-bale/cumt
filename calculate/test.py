import json



gan_jian=[{'xu_hao': 0, 'jie_dian': [0, 1], 'L': 5000},\
   {'xu_hao': 1, 'jie_dian': [1, 2], 'L': 5590, 'cos': 0.447, 'sin': -0.895}]

force=[{'xu_hao':0,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':30000,'a': 90},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'01','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':20000000},\
       {'xu_hao':2,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':50000}]


# force1=[{'xu_hao':0,'wei_zhi':[0,0],'lei_xing':'00','F':1,'a':0,'cos':0,'sin':0}]
# force2=[{'xu_hao':0,'wei_zhi':[1,2],'lei_xing':'5','chang_du':100,'duan_dian':[10,10],'duan_dian_zhi':[1,1],'a':0,'cos':0,'sin':0}]

gan_jian2=[{'xu_hao': 0, 'jie_dian': [0, 1], 'E': 1, 'A': 4, 'I': 1, 'L': 4000, 'a': 90, 'cos': 0, 'sin': 0},\
            {'xu_hao': 1, 'jie_dian': [1, 2], 'E': 1, 'A': 4, 'I': 1, 'L': 4000, 'a': 0, 'cos': 0.447, 'sin': -0.895},\
            {'xu_hao': 1, 'jie_dian': [2, 3], 'E': 1, 'A': 4, 'I': 1, 'L': 4000, 'a': 0, 'cos': 0.447, 'sin': -0.895}]
force2=[{'xu_hao':0,'wei_zhi':[0,1],'lei_xing':'10','L':0,'duan_dian':[2000,2000],'duan_dian_zhi':[15000,15000],'F':15000,'a': 90, 'cos': 0, 'sin': 0},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[10000,10000],'F':10000,'a': 0, 'cos': 0, 'sin': 0},\
       {'xu_hao':2,'wei_zhi':[1,1],'lei_xing':'02','L':0,'duan_dian':[0,0],'duan_dian_zhi':[-8000000,-8000000],'F':-8000000,'a': 0, 'cos': 0, 'sin': 0}]


gan_jian3=[{'xu_hao': 0, 'jie_dian': [0, 1], 'E': 210000, 'A': 400000, 'I': 40000000000, 'L': 5000, 'a': 0, 'cos': 0, 'sin': 0},\
   {'xu_hao': 1, 'jie_dian': [1, 2], 'E': 210000, 'A': 400000, 'I': 40000000000, 'L': 5590, 'a': 0, 'cos': 0.447, 'sin': -0.895}]
force3=[{'xu_hao':0,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':30000,'a': 90, 'cos': 0, 'sin': 0},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'02','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':20000000,'a': 0, 'cos': 0, 'sin': 0},\
       {'xu_hao':2,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':50000,'a': 0, 'cos': 0, 'sin': 0}]


gan_jian4=[{'xu_hao': 0, 'jie_dian': [0, 1], 'E': 210000, 'A': 400000, 'I': 40000000000, 'L': 5000, 'a': 0, 'cos': 0, 'sin': 0},\
   {'xu_hao': 1, 'jie_dian': [1, 2], 'E': 210000, 'A': 400000, 'I': 40000000000, 'L': 5590, 'a': 0, 'cos': 0.447, 'sin': -0.895}]
force4=[{'xu_hao':0,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':30000,'a': 90, 'cos': 0, 'sin': 0},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'02','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':20000000,'a': 0, 'cos': 0, 'sin': 0},\
       {'xu_hao':2,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':50000,'a': 0, 'cos': 0, 'sin': 0}]







##with open('gan_jian_lib.json','r',encoding='utf-8') as f:
##    c=json.load(f)



    

with open('./force.json','w',encoding='utf-8') as f:
    json.dump(force,f,ensure_ascii=False,indent=2)
with open('./gan_jian_lib.json','w',encoding='utf-8') as f:
    json.dump(gan_jian,f,ensure_ascii=False,indent=2)


# with open('gan_jian_lib.json','r',encoding='utf-8') as f:
#     c=json.load(f)
# print(c)