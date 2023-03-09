a=int(input("enter the date:"))
b=int(input("enter the month:"))
c=int(input("enter the year:"))
print("date:",a,"/",b,"/",c)
if c%4==0:
    print("given year is leap year")
else:
    print("given year is not a leap year")
