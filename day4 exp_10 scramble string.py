import random

def isScramble(s1,s2):
    if sorted(s1) != sorted(s2):
        return False
    if len(s1) <= 1:
        return True
    for i in range(1, len(s1)):
        if isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]):
            return True
        if isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i]):
            return True
    return False
s1=input("enter the str s1:")
s2=input("enter the str s2:")
print(isScramble(s1,s2))
