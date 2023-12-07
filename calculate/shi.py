a=[[0, 1, 1, 1, 0], [1, 1, 1, 1, 0]]
b=[0,1,2,3]
c=[1,2,3]
print([x+y for x,y in zip(c,b[0:3])])
ff=123
print('%d'%ff)
jj=3
print([i for i in range(3)])
dd=[[1,2],[1,2,3]]
print(sum(len(l) for l in dd))
print(list(range(10)))
tt=zip([4,5,6,7,8,9],list(range(6)))
for i in tt:
    print(i)
print(tt)