a=[]
m=int(input("enter the number 1:"))
for i in range(0,m):
    x=int(input("enter the numbers:"))
    a.append(x)
print("a:",a)
b=[]
n=int(input("enter the number 2:"))
for j in range(0,n):
    y=int(input("enter the numbers:"))
    b.append(y)
print("b:",b)
c=a+b
d=sorted(c)
print("d:",d)
