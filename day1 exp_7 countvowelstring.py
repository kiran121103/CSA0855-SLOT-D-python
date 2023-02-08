def countstring(n,s):
    if n==0:
        return 1
    count=0
    for i in range(s,5):
        count+=countstring(n-1,i)
    return count
def vowelsstring(n):
    return countstring(n,0)
n=int(input("enter the n:"))
print(vowelsstring(n))
