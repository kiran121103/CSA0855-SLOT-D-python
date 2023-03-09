string = input("Enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
num_vowels = 0
for char in string:
    if char.lower() in vowels:
        num_vowels += 1
print("Number of vowels :", num_vowels)
