list=[]
a=int(input("enter the number of numbers:"))
for i in range(0,a):
    b=int(input("enter the numbers:"))
    list.append(b)
list.sort()
print("list:",list)
p=int(input("enter the mth maximum number:"))
q=int(input("enter the nth minimum number:"))
x=list[-p]
y=list[q-1]
print("maximum number:",x)
print("minimum number:",y)
print("sum:",x+y)
print("difference:",x-y)
