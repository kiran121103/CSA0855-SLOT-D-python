def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter the number of numbers: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter a number: ")))

prime_count = 0
composite_count = 0

for num in numbers:
    if is_prime(num):
        prime_count += 1
    else:
        composite_count += 1

print("Composite number:", composite_count)
print("Prime number:", prime_count)
