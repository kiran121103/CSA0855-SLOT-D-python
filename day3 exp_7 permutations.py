from itertools import permutations
nums=[]
m=int(input("enter the number:" ))
for i in range(0,m):
    a=int(input("enter the numbers:" ))
    nums.append(a)
print("nums:",nums)
p=list(permutations(nums))
print(p)
