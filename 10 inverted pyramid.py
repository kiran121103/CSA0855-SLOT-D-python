n = int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i*2-1):
        print("*", end="")
    print()
