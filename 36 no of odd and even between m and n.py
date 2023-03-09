M = int(input("Enter the starting number: "))
N = int(input("Enter the ending number: "))

odd = 0
even = 0

for i in range(M, N+1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of Odd Numbers :", odd)
print("Number of Even Numbers :", even)
