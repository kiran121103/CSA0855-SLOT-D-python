list=[]
n=int(input("enter the range:"))
for i in range(0,n):
    a=int(input("enter the number:"))
    list.append(a)
    list.sort()
print(list)
p=int(input("enter the nth largest number:"))
x=list[-p]
print(p,"th largest number:",x)
    
