def perfectsquares(n):
    squares = [0] * (n+1)    
    for i in range(1, n+1):      
        j = 1
        while j*j <= i:            
            squares[i] = min(squares[i] or float('inf'),squares[i-j*j] + 1)
            j += 1
    return squares[n]
n=int(input("enter the number: "))
print(perfectsquares(n))
