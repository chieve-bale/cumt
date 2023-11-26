## 结构力学求解器cumt
### 单位统一为：长度mm，力N，应力MPa，默认E=206000MPa ，角度默认 °（逆时针为正）

力的类型有待商榷

***杆件索引使用杆件的编码不使用节点编码！！！***

***中间过程的数据交换尽量使用json，并确认（ensure_ascii=False, encoding='utf-8'）这两项参数以保证中文的正确显示可可读性。***

**计算程序读取杆件gan_jian_lib.json。序号、节点(类型为元组)为必须参数，杆件角度或三角函数值二选一。** 格式如下：

[
    {'xu_hao':0,'jie_dian':(0,1),'E':206000,'A':1,'I':1,'L':1,'a':0,'cos':0,'sin':0},
    {'xu_hao':1,'jie_dian':(1,2),'E':206000,'A':1,'I':1,'L':1,'a':0,'cos':0,'sin':0},
    {'xu_hao':2,'jie_dian':(3,7),'E':206000,'A':1,'I':1,'L':1,'a':0,'cos':0,'sin':0},
    {'xu_hao':3,'jie_dian':(3,4),'A':1,'I':1,'L':1,'a':0,'cos':0,'sin':0},
    {'xu_hao':4,'jie_dian':(5,7),'E':206000,'I':1,'L':1,'a':0,'cos':0,'sin':0},
    {'xu_hao':0,'jie_dian':(0,0),'E':206000,'A':1,'L':1,'a':0,'cos':0,'sin':0},
    {'xu_hao':0,'jie_dian':(0,0),'E':206000,'A':1,'I':1,'a':0,'cos':0,'sin':0},
    {'xu_hao':0,'jie_dian':(0,0),'E':206000,'A':1,'I':1,'L':1,'cos':0,'sin':0},
    {'xu_hao':0,'jie_dian':(0,0),'E':206000,'A':1,'I':1,'L':1,'a':0},
]


**计算程序读取力的json文件为force.json**。格式如下：（有待商榷！！）
[
    {'xu_hao':0,'wei_zhi':[0,0],'lei_xing':'00','chang_du':1,'duan_dian':[10,10]'duan_dian_zhi':[1,1],'F':1,'a':0,'cos':0,'sin':0}
    {'xu_hao':0,'wei_zhi':[0,0],'lei_xing':'00','F':1,'a':0,'cos':0,'sin':0}
    {'xu_hao':0,'wei_zhi':[1,2],'lei_xing':'5','chang_du':100,'duan_dian':[10,10],'duan_dian_zhi':[1,1],'a':0,'cos':0,'sin':0}


]
