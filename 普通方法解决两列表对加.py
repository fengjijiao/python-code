a=[1,2,3,4,5,6]
b=[6,7,8,9,10,11]
d=[]
l=len(a) if len(a)<len(b) else len(b)
for i in range(l):
    d.append(a[i]+b[i])
print(d)