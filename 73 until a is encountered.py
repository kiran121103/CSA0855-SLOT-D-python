upper_count = 0
lower_count = 0
num_count = 0
while True:
    char = input("Enter any character: ")
    if char == '*':
        break  
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        num_count += 1
print("Total count of lower case:", lower_count)
print("Total count of upper case:", upper_count)
print("Total count of numbers =", num_count)
