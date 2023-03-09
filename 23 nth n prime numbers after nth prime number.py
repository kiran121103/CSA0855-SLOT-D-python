def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_and_next_primes(n, m):
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                print(f"{n}th Prime number is {num}")
                break
        num += 1
    
    prime_list = []
    while len(prime_list) < m:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    
    print(f"{m} prime numbers after {n}th Prime number are:", end=" ")
    print(*prime_list, sep=", ")
    
nth_and_next_primes(3, 3)
