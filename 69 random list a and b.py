import random

a = int(input("Enter A Value: "))
b = int(input("Enter B Value: "))
n = int(input("Enter number of elements: "))

random_list = []
for i in range(n):
    random_list.append(random.randint(a, b))

print("Randomized list is:", random_list)
