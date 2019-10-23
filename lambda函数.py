numbers=[0,1,2,3,4,5,6,7,8,9]
lam=lambda x:x+3
n=[]
for i in numbers:
    n.append(lam(i))

print(n)

g=lambda x,y:x**y
n=4
print([g(n,i) for i in range(n)])

for i in range(n):
   print((lambda x:x**2)(i))