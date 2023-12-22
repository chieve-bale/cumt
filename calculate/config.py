import json
###在config里面加入你的设置内容
config={'gan_jian':{'E': 210000, 'A': 400000, 'I': 40000000000,'L':1,'a':0,'cos':0,'sin':0,'lian_jie':[4,4]},\
         'he_zai':{'L':0,'a':0,'cos':0,'sin':0,'duan_dian_jv':[0,0],'duan_dian_zhi':[0,0]}}

# config={'gan_jian':{'E': 1, 'A': 1, 'I': 4,'L':1,'a':0,'cos':0,'sin':0,'lian_jie':[4,4]},\
#          'force':{'L':0,'a':0,'cos':0,'sin':0,'duan_dian':[0,0],'duan_dian_zhi':[0,0]}}


##写入‘config’文件
with open('config',mode='w',encoding='utf-8') as f:
    json.dump(config,f,ensure_ascii=False,indent=2)