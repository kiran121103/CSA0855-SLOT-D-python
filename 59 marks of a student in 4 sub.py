a=int(input("enter the marks of python:"))
b=int(input("enter the marks of c programming:"))
c=int(input("enter the marks of mathematics:"))
d=int(input("enter the marks of physics:"))
total=a+b+c+d
print("total:",total)
aggregate=(total/4)
print("aggregate:",aggregate)
if aggregate>=75:
    print("DISTINCTION")
elif aggregate<75 and aggregate>=60:
    print("FIRST DIVISION")
elif aggregate<60 and aggregate>=50:
    print("SECOND DIVISION")
elif aggregate<50 and aggregate>=40:
    print("THIRD DIVISION")
else:
    print("FAIL")
