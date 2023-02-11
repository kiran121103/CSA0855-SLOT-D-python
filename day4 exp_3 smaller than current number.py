def smallerNumbersThanCurrent(nums):
    count=[0]*len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j]<nums[i]and j!=i:
                count[i]+=1
    return count

print(smallerNumbersThanCurrent([8,1,2,2,3]))
print(smallerNumbersThanCurrent([6,5,4,8]))
print(smallerNumbersThanCurrent([7,7,7,7]))
        
