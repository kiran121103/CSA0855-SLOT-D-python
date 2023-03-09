symbol=input("enter the symbol:")
width = int(input("enter the width:"))
height = int(input("enter the height"))
for i in range(height):
    if i==0 or i==height-1:
        print(symbol * width)
    else:
        print(symbol+" "*(width-2)+symbol)
