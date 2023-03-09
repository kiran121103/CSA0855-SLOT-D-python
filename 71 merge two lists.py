list1=[]
n=int(input("enter the number of numbers:"))
for i in range(0,n):
    a=int(input("enter the numbers:"))
    list1.append(a)
print("list1:",list1)

list2=[]
m=int(input("enter the number of numbers:"))
for j in range(0,m):
    b=int(input("enter the numbers:"))
    list2.append(b)
print("list2:",list2)

list=list1+list2
list.sort()
print("list3:",list)

