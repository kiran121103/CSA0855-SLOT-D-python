M = int(input("Enter the value of M: "))
N = int(input("Enter the value of N: "))
K = int(input("Enter the value of K: "))

for num in range(M, N+1, K+1):
    print(num, end=", ")
