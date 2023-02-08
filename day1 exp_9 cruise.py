def cruise (T,L,E):
    maxguests=0
    guests=0
    for i in range(T):
        guests+=E[i]-L[i]
        maxguests=max(maxguests,guests)

    return maxguests

T=5
E=[7,0,5,1,3]
L=[1,2,1,3,4]
print(cruise(T,L,E))
T=-4
E=[1,5,9,10]
L=[0,2,3,4]
print(cruise(T,L,E))
T=0
E=[10,2,3,4]
L=[1234]
print(cruise(T,L,E))
