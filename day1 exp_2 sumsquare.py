a=[]
n=int(input("enter the number:"))
for i in range(1,n+1):
    b=int(input("enter the number:"))
    a.append(b)
    
def sumsquare(a):
    odd=0
    even=0
    for i in a:
        if i%2==0:
            even=even+i**2
        else:
            odd=odd+i**2
    a=[odd,even]
    return (a)
print(sumsquare(a))
    

