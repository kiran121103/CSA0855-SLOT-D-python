arr = []
a=int(input("enter the range:"))
for i in range(0,a):
    b=int(input("enter the numbers:"))
    arr.append(b)
print("array of elements:",arr)
arr=arr[::-1]
print("reverse array elements:",arr)
