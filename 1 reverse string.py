str=input("Enter a str: ")
reverse_str=""
for i in range(len(str)-1,-1,-1):
    reverse_str+=str[i]
print("Reverse String: "+reverse_str)
