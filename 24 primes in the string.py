def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

arr = []
a=int(input("enter the range:"))
for j in range(0,a):
    b=int(input("enter the numbers:"))
    arr.append(b)
print("arr:",arr)
primes = []
for num in arr:
    if is_prime(num):
        primes.append(num)

print("Prime numbers in array elements:", primes)
