try:
    dec = int(input("Decimal Number: "))
except:
    print("Invalid input. Please enter a valid decimal number.")
else:
    binary = bin(dec)[2:]
    octal = oct(dec)[2:]
    print("Binary Number =", binary)
    print("Octal =", octal)
