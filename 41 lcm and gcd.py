n = int(input("Enter N value: "))
nums = []
for i in range(n):
    num = int(input("enter the numbers:"))
    nums.append(num)
    
def lcm(a, b):
    return (a * b) // gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

lcm_num = nums[0]
for i in range(1, n):
    lcm_num = lcm(lcm_num, nums[i])

gcd_num = nums[0]
for i in range(1, n):
    gcd_num = gcd(gcd_num, nums[i])

print("LCM =", lcm_num)
print("GCD =", gcd_num)
