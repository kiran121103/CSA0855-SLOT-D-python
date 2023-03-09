size = int(input("Enter pyramid size: "))
for i in range(size, 0, -1):
    print(" "*(size-i), end="")
    print("*"*(2*i-1))
