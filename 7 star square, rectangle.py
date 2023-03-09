size=int(input("enter the size:"))
for i in range(size):
    print("*"*size)

width=int(input("enter the width:"))
height=int(input("enter the height:"))
for i in range(height):
    if i==0 or i==height-1:
        print("$" * width)
    else:
        print("$"+" "*(width-2)+"$")
