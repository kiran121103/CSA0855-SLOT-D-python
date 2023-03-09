rows = int(input("enter the rows:"))
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    for j in range(i+1):
        if j == 0:
            num = 1
        elif j % 2 == 1:
            num = -j
        else:
            num = j
        print("{0:4}".format(num), end="")
    print()

