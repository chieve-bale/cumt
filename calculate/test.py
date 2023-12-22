import json



gan_jian20=[{'xu_hao': 0, 'jie_dian': [0, 1], 'L': 5000},\
   {'xu_hao': 1, 'jie_dian': [1, 2], 'L': 5590, 'cos': 0.447, 'sin': -0.895}]

he_zai20=[{'xu_hao':0,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian_jv':[0,0],'duan_dian_zhi':[30000,0],'F':30000,'a': 90},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'01','L':0,'duan_dian_jv':[0,0],'duan_dian_zhi':[30000,0],'F':20000000},\
       {'xu_hao':2,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian_jv':[0,0],'duan_dian_zhi':[30000,0],'F':50000}]


# he_zai1=[{'xu_hao':0,'wei_zhi':[0,0],'lei_xing':'00','F':1,'a':0,'cos':0,'sin':0}]
# he_zai2=[{'xu_hao':0,'wei_zhi':[1,2],'lei_xing':'5','chang_du':100,'duan_dian':[10,10],'duan_dian_zhi':[1,1],'a':0,'cos':0,'sin':0}]

gan_jian2=[{'xu_hao': 0, 'jie_dian': [0, 1],  'L': 4000, 'a': 90},\
            {'xu_hao': 1, 'jie_dian': [1, 2], 'E': 1, 'A': 4, 'I': 1, 'L': 4000, 'a': 0, 'cos': 0.447, 'sin': -0.895},\
            {'xu_hao': 1, 'jie_dian': [2, 3], 'E': 1, 'A': 4, 'I': 1, 'L': 4000, 'a': 0, 'cos': 0.447, 'sin': -0.895}]
he_zai2=[{'xu_hao':0,'wei_zhi':[0,1],'lei_xing':'10','L':0,'duan_dian_jv':[2000,2000],'duan_dian_zhi':[15000,15000],'F':15000,'a': 90, 'cos': 0, 'sin': 0},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'00','L':0,'duan_dian_jv':[0,0],'duan_dian_zhi':[10000,10000],'F':10000,'a': 0, 'cos': 0, 'sin': 0},\
       {'xu_hao':2,'wei_zhi':[1,1],'lei_xing':'02','L':0,'duan_dian_jv':[0,0],'duan_dian_zhi':[-8000000,-8000000],'F':-8000000,'a': 0, 'cos': 0, 'sin': 0}]


gan_jian38=[{'xu_hao': 0, 'jie_dian': [0, 1], 'lian_jie':[10,0],'E': 4, 'A': 1, 'I': 4, 'L': 4, 'a': 90},\
              {'xu_hao': 1, 'jie_dian': [1, 2], 'lian_jie':[0,1],'E': 4, 'A': 1, 'I': 4, 'L': 4},\
              {'xu_hao': 2, 'jie_dian': [2, 3], 'lian_jie':[1,10],'E':4,'A': 1, 'I': 4,'L': 4}]

he_zai38=[{'xu_hao':0,'wei_zhi':[0,1],'lei_xing':'10','duan_dian_jv':[2000,2000],'F':15000},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'00','F':10000},\
       {'xu_hao':2,'wei_zhi':[1,1],'lei_xing':'01','F':-8000000},\
       {'xu_hao':3,'wei_zhi':[1,2],'lei_xing':'3','L':4000,'duan_dian_jv':[0,0],'duan_dian_zhi':[-8,-8],'F':-8},\
       {'xu_hao':4,'wei_zhi':[2,2],'lei_xing':'00','F':-16000,'a': 90},\
       {'xu_hao':5,'wei_zhi':[2,3],'lei_xing':'3','L':4000,'duan_dian_jv':[0,0],'duan_dian_zhi':[-8,-8],'F':-8}]


gan_jian35=[{'xu_hao': 0, 'jie_dian': [0, 1], 'E':7500000,'L': 6000},\
              {'xu_hao': 1, 'jie_dian': [1, 2], 'E':15000000,'L': 8000},\
              {'xu_hao': 2, 'jie_dian': [2, 3], 'E':10000000,'L': 6000}]
he_zai35=[{'xu_hao':0,'wei_zhi':[0,1],'lei_xing':'3','L':6000,'duan_dian_jv':[0,0],'duan_dian_zhi':[-10,-10],'F':-10},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'01','F':-60000000},\
       {'xu_hao':2,'wei_zhi':[1,2],'lei_xing':'10','duan_dian_jv':[4000,4000],'F':-20000,'a':90},\
       {'xu_hao':3,'wei_zhi':[2,2],'lei_xing':'01','F':50000000},\
       {'xu_hao':4,'wei_zhi':[3,3],'lei_xing':'01','F':30000000}]


gan_jian31=[{'xu_hao': 0, 'jie_dian': [0, 1], 'lian_jie':[0,0],'L': 5000},\
              {'xu_hao': 1, 'jie_dian': [1, 2], 'lian_jie':[0,0],'L': 5590, 'cos': 0.447, 'sin': -0.895}]
he_zai31=[{'xu_hao':0,'wei_zhi':[1,1],'lei_xing':'00','F':30000,'a': 90},\
       {'xu_hao':1,'wei_zhi':[1,1],'lei_xing':'01','F':20000000},\
       {'xu_hao':2,'wei_zhi':[1,1],'lei_xing':'00','F':50000},\
       {'xu_hao':3,'wei_zhi':[0,1],'lei_xing':'3','L':5000,'duan_dian_jv':[0,0],'duan_dian_zhi':[-18,-18],'F':-18}]




##with open('gan_jian_lib.json','r',encoding='utf-8') as f:
##    c=json.load(f)

date={'gan_jian':[],'he_zai':[],'force':[],'wei_yi':[]}

with open('./can_shu.json','r',encoding='utf-8') as f:
    date.update(json.load(f))

with open('./can_shu.json','w',encoding='utf-8') as f:
     date['gan_jian']=gan_jian38
     date['he_zai']=he_zai38
     json.dump(date,f,ensure_ascii=False,indent=2)
