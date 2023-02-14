nums=[]
a=int(input("enter the range: "))
for i in range(0,a):
    b=int(input("enter the nums:"))
    nums.append(b)
print("nums:",nums)

n = len(nums)
left, right = 0, n - 1
while left < right:
    m = (left + right) // 2
    left = m + 1
    right = m
    if nums[m] < nums[m+1]:
        print(left)
    else:
        print(right)

