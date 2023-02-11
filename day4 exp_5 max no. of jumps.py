def minjumps(arr):
    n=len(arr)
    jumps=[float("inf")]*n
    jumps[0]=0
    
    for i in range(1, n):
        for j in range(i):
            if i <= j+arr[j] and jumps[j] != float("inf"):
                jumps[i]=min(jumps[i],jumps[j]+1)
                break
    return jumps[n-1] if jumps[n-1] != float("inf") else -1
arr=[]
a=int(input("enter the number:"))
for i in range(0,a):
    b=int(input("enter the number:"))
    arr.append(b)
print("arr:",arr)
print(minjumps(arr))
