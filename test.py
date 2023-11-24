class gan_jian:
    i=1
    def __init__(self,i,L):
        self.i=i
        self.L=L
    def ff(self,gg):  ##输入杆件代码,代码为数字字符，输出刚度矩阵。按照课本P227表格顺序
        i=self.i
        L=self.L
        match gg:
            case '00':
                return [[i        ,0         ,0         ,-i      ,0         ,0       ],\
                        [0        ,12*i/L/L  ,6*i/L     ,0       ,-12*i/L/L ,6*i/L    ],\
                        [0        ,6*i/L     ,4*i       ,0       ,-6*i/L    ,2*i      ],\
                        [-i       ,0         ,0         ,-i      ,0         ,0       ],\
                        [0        ,-12*i/L/L ,-6*i/L    ,0       ,12*i/L/L  ,-6*i/L   ],\
                        [0        ,6*i/L     ,2*i       ,0       ,-6*i/L    ,4*i      ]]
            case '01':
                return [[]]
            case '02':
                return [[]]
        
print(gan_jian(1,1).ff('00'))
