a = int(input("Enter lower range: "))
b = int(input("Enter upper range: "))
c = []
for i in range(a, b+1):
    if (i**0.5).is_integer() and sum(int(digit) for digit in str(i)) < 10:
        c.append(i)
print(c)
