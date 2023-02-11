def is_palindrome(s):
    s = s.lower()
    s = [c for c in s if c.isalnum()]
    return True if s == s[::-1] else False

s = input("enter the string:")
print(is_palindrome(s))
