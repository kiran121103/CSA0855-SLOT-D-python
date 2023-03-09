def composite(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
arr = []
a=int(input("enter the range:"))
for j in range(0,a):
    b=int(input("enter the numbers:"))
    arr.append(b)
print("arr:",arr)
count = 0
for num in arr:
    if composite(num):
        count+=1
print("Number of Composite Numbers =",count)
