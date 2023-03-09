n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print("{:.2f}".format((i+1)**2/(j+1)**2), end=" ")
    print()
