import math
num = int(input("Enter the number: "))
sqrt = math.sqrt(num)
if int(sqrt) == sqrt:
    print("Square Root: ",(int(sqrt), -int(sqrt)))
else:
    print("given number is not a perfect square.")
