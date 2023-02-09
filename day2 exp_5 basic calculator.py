a=float(input("enter first number:"))
b=float(input("enter second number:"))

print("press 1 for + \npress 2 for - \npress 3 for * \npress 4 for /")

choice=int(input("select choice from 1-4:"))

if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
elif choice == 4:
    print(a/b)
