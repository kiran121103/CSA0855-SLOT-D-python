def palindrome(a):
    return a==a[::-1]
    
a=str(input("enter the number:"))
if a==a[::-1]:
    print("panlindrome")
else:
    print("it is not a palindrone")
