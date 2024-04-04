def matrix_multiply(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

a = [[1, 0, 0], 
     [0, 1, 0],
     [0, 0, 1]]
b = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

c = matrix_multiply(a, b)
print(c)