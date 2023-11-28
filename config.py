import json
###在config里面加入你的设置内容
config={'gan_jian':{'xu_hao':0,'jie_dian':[0,1], 'E': 210000, 'A': 400000, 'I': 40000000000,'L':1,'a':0,'cos':0,'sin':0},\
        'force':{'xu_hao':0,'wei_zhi':[0,0],'lei_xing':'00','L':0,'duan_dian':[0,0],'duan_dian_zhi':[1,1],'F':1,'a':0,'cos':0,'sin':0}}
##写入‘config’文件
with open('config',mode='w',encoding='utf-8') as f:
    json.dump(config,f,ensure_ascii=False,indent=2)