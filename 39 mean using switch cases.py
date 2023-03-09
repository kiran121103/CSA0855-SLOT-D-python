n = int(input("Enter N value: "))
case = int(input("Enter case (1-4): "))

if case == 1:  
    odd = 0
    for i in range(1,2*n,2):
        odd += i
    mean = odd / n
    print("Mean of first", n, "odd numbers:", mean)

elif case == 2:  
    even= 0
    for i in range(2, 2*n+1, 2):
        even += i
    mean = even / n
    print("Mean of first", n, "even numbers:", mean)

elif case == 3:
    square = 0
    for i in range(1, n+1):
        square += i**2
    mean = square / n
    print("Mean of first", n, "square numbers:", mean)

elif case == 4:
    cube = 0
    for i in range(1, n+1):
        cube += i**3
    mean = cube / n
    print("Mean of first", n, "cube numbers:", mean)

else:
    print("Invalid case number entered.")
