num = int(input("Enter number: "))
num_str = str(num)
num_digits = len(num_str)
sum = 0
for digit in num_str:
    sum += int(digit)**num_digits
if sum == num:
    print("Given number is Armstrong number")
else:
    print("Given number is not Armstrong number")
