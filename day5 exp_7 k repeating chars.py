def longestSubstring(s, k):
    if len(s) < k:
        return 0
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in count:
        if count[c] < k:
            return max(longestSubstring(sub, k) for sub in s.split(c))
    return len(s)
s=input("enter the string:")
k=int(input("enter the number:"))
print(longestSubstring(s,k))
