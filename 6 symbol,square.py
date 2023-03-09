symbol = input("Enter the symbol to use: ")
size = int(input("Enter the size of the square: "))
print(symbol*size)
for i in range(size-2):
    print(symbol+" "*(size-2)+symbol)
if size>1:
    print(symbol*size)
