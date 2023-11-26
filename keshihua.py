import turtle as tl
import numpy as np
import json

tl.setup(1000,1000) #设置画布大小
tl.pencolor("black")
tl.width(2)
tl.speed(0)



#获取杆件的长度以及角度
a=[{'xu_hao':0,'jie_dian':(0,1),'E':210000,'A':400000,'I':40000000000,'L':200,'a':0,'cos':0,'sin':0},{'xu_hao':1,'jie_dian':(1,2),'E':210000,'A':400000,'I':40000000000,'L':100,'a':45,'cos':0.447,'sin':-0.895}]

for i in a:
    L = i['L']
    a = i['a']
    tl.left(a)
    tl.forward(L)
tl.ht()
tl.done()