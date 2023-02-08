def isIsomorphic(s,t):          
    if(len(s)!= len(t)):
                return false
    a=[s.count(char1) for char1 in s]
    b=[t.count(char1) for char1 in t]
    return a==b

print(isIsomorphic("egg", "add"))        
print(isIsomorphic("foo", "bar"))      
print(isIsomorphic("paper", "title"))   
print(isIsomorphic("fry", "sky"))
print(isIsomorphic("aples","apple"))
