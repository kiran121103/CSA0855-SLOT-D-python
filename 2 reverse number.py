num=int(input("enter  the number:"))
reverse_num=0
while num != 0:
    digit=num%10
    num=num//10
    reverse_num=(reverse_num*10)+digit
print("reverse number:",reverse_num)
    
