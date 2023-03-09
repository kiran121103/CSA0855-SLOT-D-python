def is_perfect(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def get_perfect_numbers(n):
    perfect_numbers = []
    num = 2
    while len(perfect_numbers) < n:
        if is_perfect(num):
            perfect_numbers.append(num)
        num += 1
    return perfect_numbers

n = int(input("enter the number:"))
perfect_numbers = get_perfect_numbers(n)
print("first", n, "perfect numbers:",perfect_numbers,end=" ,")
