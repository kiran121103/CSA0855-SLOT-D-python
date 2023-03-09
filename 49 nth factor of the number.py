num = int(input("Enter a number: "))
n = int(input("Enter the value of n: "))

count = 0

for i in range(1, num+1):
    if num % i == 0:
        count += 1
        if count == n:
            print(n,"th factor of",num,"=", i)
        

