a=int(input("enter the income:"))
if a<=150000:
    b=0
elif a>=150001 and a<=300000:
    b=0.10
elif a>=300001 and a<=500000:
    b=0.20
elif a>=500001 :
    b=0.30
tax=a*b
print("tax:",int(tax))
