import json



gan_jian20=[{'xu_hao': 0, 'jie_dian': [0, 1], 'L': 5000},\
   {'xu_hao': 1, 'jie_dian': [1, 2], 'L': 5590, 'cos': 0.447, 'sin': -0.895}]

force20=[{'xu_hao':0,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':30000,'a': 90},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'01','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':20000000},\
       {'xu_hao':2,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':50000}]


# force1=[{'xu_hao':0,'wei_zhi':[0,0],'lei_xing':'00','F':1,'a':0,'cos':0,'sin':0}]
# force2=[{'xu_hao':0,'wei_zhi':[1,2],'lei_xing':'5','chang_du':100,'duan_dian':[10,10],'duan_dian_zhi':[1,1],'a':0,'cos':0,'sin':0}]

gan_jian2=[{'xu_hao': 0, 'jie_dian': [0, 1],  'L': 4000, 'a': 90},\
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


gan_jian35=[{'xu_hao': 0, 'jie_dian': [0, 1], 'L': 6000},\
              {'xu_hao': 1, 'jie_dian': [1, 2], 'L': 8000},\
              {'xu_hao': 3, 'jie_dian': [2, 3], 'L': 6000}]
force35=[{'xu_hao':0,'wei_zhi':[0,1],'lei_xing':'3','L':6000,'duan_dian':[0,0],'duan_dian_zhi':[-10,-10],'F':-10},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'01','F':-60000000},\
       {'xu_hao':2,'wei_zhi':[1,2],'lei_xing':'11','duan_dian':[4000,4000],'F':-20000},\
       {'xu_hao':3,'wei_zhi':[2,2],'lei_xing':'01','F':50000000},\
       {'xu_hao':4,'wei_zhi':[3,3],'lei_xing':'01','F':30000000}]


gan_jian31=[{'xu_hao': 0, 'jie_dian': [0, 1], 'L': 5000},\
              {'xu_hao': 1, 'jie_dian': [1, 2], 'L': 5590, 'cos': 0.447, 'sin': -0.895}]
force31=[{'xu_hao':0,'wei_zhi':[1,1],'lei_xing':'00','F':30000,'a': 90},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'01','F':20000000},\
       {'xu_hao':2,'wei_zhi':[1,1],'lei_xing':'00','F':50000},\
       {'xu_hao':3,'wei_zhi':[0,1],'lei_xing':'3','L':5000,'duan_dian':[0,0],'duan_dian_zhi':[-18,-18],'F':-18}]




##with open('gan_jian_lib.json','r',encoding='utf-8') as f:
##    c=json.load(f)



    

with open('./force.json','w',encoding='utf-8') as f:
    json.dump(force31,f,ensure_ascii=False,indent=2)
with open('./gan_jian_lib.json','w',encoding='utf-8') as f:
    json.dump(gan_jian31,f,ensure_ascii=False,indent=2)


# with open('gan_jian_lib.json','r',encoding='utf-8') as f:
#     c=json.load(f)
# print(c)