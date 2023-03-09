n=int(input("enter the rows:"))
for i in range(n):
    print(" "*(2*(n-i-1)),end="")
    num=1
    for j in range(i+1):
        print(f"{num:3d}",end="")
        num=num*(i-j)//(j+1)
    print()
