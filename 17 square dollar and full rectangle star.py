size = int(input("enter the size:"))
symbol = "$"
print(symbol*size)
for i in range(size-2):
    print(symbol + " "*(size-2) + symbol)
print(symbol*size)
width = int(input("enter the width:"))
height = int(input("enter the sheight:"))
symbol = "*"
for i in range(height):
    for j in range(width):
        print(symbol, end="")
    print()
