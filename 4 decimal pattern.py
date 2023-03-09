n=int(input("enter the rows:"))
for i in range(1, n+1):
    print(" "*(n-i),end="")    
    for j in range(1,i+1):
        print(j/10, end="")
    print() 
