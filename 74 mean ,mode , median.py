array=[]
n=int(input("enter the number of numbers:"))
for i in range(0,n):
    a=int(input("enter the numbers:"))
    array.append(a)
print("array:",array)
import statistics
mean = sum(array) / len(array)
print("Mean =", mean)
median = statistics.median(array)
print("Median =", median)
mode = statistics.mode(array)
print("Mode =", mode)
