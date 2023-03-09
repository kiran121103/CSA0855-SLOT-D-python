num=input("enter the number to be printed:")
n=int(input("max number of times to print:"))
for i in range(n):
    print(num*(i+1))
for i in range(n-1):
    print(num*(n-i-1))
