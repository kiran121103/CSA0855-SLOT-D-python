M = int(input("Enter the starting number: "))
N = int(input("Enter the ending number: "))

odd_numbers = []
even_numbers = []

for i in range(M, N+1):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("even_numbers:",even_numbers)
print("odd_numbers:",odd_numbers)
