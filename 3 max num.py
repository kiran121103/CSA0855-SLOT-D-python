a=[]
n=int(input("entre the range:"))
for i in range(0,n):
    b=int(input("enter the numbers:"))
    a.append(b)
print(a)
max_num=a[0]
for i in a:
    if i>max_num:
        max_num=i
print("maximum number:",max_num)
