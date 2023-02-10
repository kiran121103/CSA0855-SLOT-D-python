def maxProfit(price,n):
    profit=[0]*n
    max_price=price[n-1]
    for i in range(n-2,0,-1):
        if price[i]>max_price:
            max_price=price[i]
        profit[i]=max(profit[i+1],max_price-price[i])
    min_price=price[0]
    for i in range(1,n):
        if price[i]<min_price:
           min_price=price[i]
        profit[i]=max(profit[i-1],profit[i]+(price[i]-min_price))
    result=profit[i-1]
    return result
price=[]
a=int(input("enter the number:"))
for j in range(0,a):
    b=int(input("enter the numbers:"))
    price.append(b)
print("price:",price)
print("maximum profit is",maxProfit(price,len(price)))
