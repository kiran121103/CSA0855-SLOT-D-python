l1=[]
a=int(input("enter the number of elemnts of l1:"))
for i in range(0,a):
    b=int(input("enter the element:"))
    l1.append(b)
l2=[]
c=int(input("enter the number of elemnts of l2:"))
for j in range(0,c):
    d=int(input("enter the element:"))
    l1.append(d)

l3=l1+l2
l4=sorted(l3)
print("shuffled list:",l4)

