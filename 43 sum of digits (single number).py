n = int(input("Enter N value:"))
num = input("Enter" + str(n)+ "digit number:")
digits_sum = sum(int(digit) for digit in num)
while digits_sum > 9:
    digits_sum = sum(int(digit) for digit in str(digits_sum))
print("Sum of", n, "digit number:", digits_sum)
