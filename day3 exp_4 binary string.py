def addbinary(a, b):
    a = int(a,2)
    b = int(b,2)
    c = a+b
    return format(c,"b")
print(addbinary("11","1"))
print(addbinary("1010","1011"))
print(addbinary("1111","1010"))

