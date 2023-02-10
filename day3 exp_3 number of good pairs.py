def goodpairs(nums):
   count=0
   n=len(nums)
   for i in range(n):
      for j in range(i+1,n):
         if nums[i] == nums[j]:
            count+=1
   return count

nums=[]
a=int(input("enter the number:"))
for k in range(0,a):
    b=int(input("enter the number:"))
    nums.append(b)
print("nums:",nums)
print(goodpairs(nums))
