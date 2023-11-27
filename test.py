import json



gan_jian=[{'xu_hao': 0, 'jie_dian': [0, 1], 'E': 210000, 'A': 400000, 'I': 40000000000, 'L': 5000, 'a': 0, 'cos': 0, 'sin': 0},\
   {'xu_hao': 1, 'jie_dian': [1, 2], 'E': 210000, 'A': 400000, 'I': 40000000000, 'L': 5590, 'a': 0, 'cos': 0.447, 'sin': -0.895}]

force=[{'xu_hao':0,'wei_zhi':[2,2],'lei_xing':'01','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':30000,'a': 0, 'cos': 0, 'sin': 0},\
       {'xu_hao':1,'wei_zhi':[2,2],'lei_xing':'04','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':20000000,'a': 0, 'cos': 0, 'sin': 0},\
       {'xu_hao':2,'wei_zhi':[2,2],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[30000,0],'F':50000,'a': 0, 'cos': 0, 'sin': 0}]


# force1=[{'xu_hao':0,'wei_zhi':[0,0],'lei_xing':'00','F':1,'a':0,'cos':0,'sin':0}]
# force2=[{'xu_hao':0,'wei_zhi':[1,2],'lei_xing':'5','chang_du':100,'duan_dian':[10,10],'duan_dian_zhi':[1,1],'a':0,'cos':0,'sin':0}]




##with open('gan_jian_lib.json','r',encoding='utf-8') as f:
##    c=json.load(f)

    
print(force)
with open('force.json','w',encoding='utf-8') as f:
    json.dump(force,f,ensure_ascii=False,indent=4)


with open('gan_jian_lib.json','r',encoding='utf-8') as f:
    c=json.load(f)
print(c)