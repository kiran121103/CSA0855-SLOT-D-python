class solution(object):
 def validnumber(n,s):
     s=s.strip()
     try:
         s=float(s)
         return True
        
     except:
        return False
a=solution()
print(a.validnumber("0"))
print(a.validnumber("e"))
print(a.validnumber(""))
print(a.validnumber("."))
print(a.validnumber("%"))
