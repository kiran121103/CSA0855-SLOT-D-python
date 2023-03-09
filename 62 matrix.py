
mat1 = [[1, 2],
        [5, 3]]

mat2 = [[2, 3],
        [4, 1]]

mat_sum = [[0, 0],
           [0, 0]]
for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat_sum[i][j] = mat1[i][j] + mat2[i][j]
print("Mat Sum ")
for row in mat_sum:
    print(row)

mat_mul = [[0, 0],
           [0, 0]]
for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
            mat_mul[i][j] += mat1[i][k] * mat2[k][j]
print("mat multiplication")
for row in mat_mul:
    print(row)
