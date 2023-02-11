def delchar(s,c):
    if len(c) != 1:
        return s
    else:
        return s.replace(c,"")

s = input("Enter the string: ")
c = input("Enter a character to be deleted: ")
print("String after the character is removed:", delchar(s, c))
