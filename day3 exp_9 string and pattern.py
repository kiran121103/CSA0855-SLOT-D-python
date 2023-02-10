import re
s = input("enter the first string:")
p = input("enter the second string:")
p = ".*".format(p)
p = re.compile(p)
if p.fullmatch(s):
    print("true")
else:
    print("false")
