class solution:
    def lettercombination(s,digits):
        if(len(digits)==0):
            return[]
        m={'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':''}
        n=['']
        for i in digits:
            b=[]
            for j in m[i]:
                b=b+[a+j for a in n]
            n=b
        return n
c=solution()
num=list(input("enter number:"))
print(c.lettercombination(num))
