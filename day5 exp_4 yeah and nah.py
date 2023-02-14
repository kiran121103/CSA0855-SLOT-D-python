num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

product = num1 * num2
sum = num1 + num2

if product % sum == 0:
    print("YEAH")
else:
    print("NAH")
