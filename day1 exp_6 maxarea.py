def maxArea(a, len) :
    area = 0
    for i in range(len) :
        for j in range(i + 1, len) :
            area = max(area, min(a[j], a[i])*(j - i))
    return area
a=[]
n=int(input("enter the number:"))
for k in range(1,n+1):
    b=int(input("enter the numbers:"))
    a.append(b)
    print(a)
len1=len(a)
print(maxArea(a, len1))
