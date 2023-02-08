def Happynum(n):
  a = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in a:
            return False
        a.add(n)
  return True
print(Happynum(19))
print(Happynum(2))
print(Happynum(1))
print(Happynum(0))
print(Happynum(5))
