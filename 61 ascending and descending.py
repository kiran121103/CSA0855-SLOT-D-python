names = []
while True:
    name = input("Enter a name (or press enter to finish): ")
    if name == "":
        break
    names.append(name)
order = input("Enter the sort order (A for ascending, D for descending): ")
if order.upper() == "A":
    names.sort()
elif order.upper() == "D":
    names.sort(reverse=True)
else:
    print("Invalid sort order entered. Please try again.")
for name in names:
    print(name)
