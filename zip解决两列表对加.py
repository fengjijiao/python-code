a=[1,2,3,4,5,6]
b=[6,7,8,9,10,11]
d=[]
for x,y in zip(a,b):
    d.append(x+y)
print(d)