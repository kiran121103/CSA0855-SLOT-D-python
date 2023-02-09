def is_match(s,p):
    m,n = len(s),len(p)
    a =[[False]*(n +1) for _ in range(m+1)]
    a[0][0] = True
    for i in range(1,n+1):
        if p[i-1]=='*':
            a[0][i]=a[0][i-2]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if p[j-1]=='.' or p[j-1]==s[i-1]:
                a[i][j]=a[i-1][j-1]
            elif p[j - 1]=='*':
                a[i][j]=a[i][j-2]or(a[i-1][j]and(s[i-1]==p[j-2] or p[j-2]=='.'))
    return a[m][n]
s = str(input("enter the string s:"))
p = str(input("enter the string p:"))
if is_match(s, p):
    print("The input string matches the pattern.")
else:
    print("The input string does not match the pattern.")

