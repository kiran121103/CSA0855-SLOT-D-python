def combination(p):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and i!=k):

                     print(p[i],p[j],p[k])
p=[1,2,3]
combination(p)
