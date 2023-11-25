import json



a=[{'xu_hao': 0, 'jie_dian': [0, 1], 'E': 210000, 'A': 400000, 'I': 40000000000, 'L': 5000, 'a': 0, 'cos': 0, 'sin': 0},\
   {'xu_hao': 1, 'jie_dian': [1, 2], 'E': 210000, 'A': 400000, 'I': 40000000000, 'L': 5590, 'a': 0, 'cos': 0.447, 'sin': -0.895}]




##with open('gan_jian_lib.json','r',encoding='utf-8') as f:
##    c=json.load(f)

    
print(a)
with open('gan_jian_lib.json','w',encoding='utf-8') as f:
    json.dump(a,f,ensure_ascii=False,indent=4)
