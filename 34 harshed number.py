n=int(input("Enter the number: "))
sum_digits = sum(int(digit) for digit in str(n))
if n % sum_digits == 0:
    print("Given number is Harshad number")
else:
    print("Given number is not a Harshad number")
