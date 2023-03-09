line = input("eneter the str:")
special_chars_count = 0
for char in line:
    if not char.isalnum() and not char.isspace():
        print(char)
        special_chars_count += 1
print("Total special characters: ",special_chars_count)
