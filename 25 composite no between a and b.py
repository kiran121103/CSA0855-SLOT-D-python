def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

composite_numbers = []

for i in range(a, b+1):
    if is_composite(i):
        composite_numbers.append(i)

print("Composite numbers between", a, "and", b, "are:")
print(composite_numbers)
