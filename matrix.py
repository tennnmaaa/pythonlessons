def get_matrix(n, m, value):
    matrix = []

    for i in range(m):
        i = []
        matrix.append(i)
        for j in range(n):
            i.append(value)
    return matrix

result1 = get_matrix(4,2,13)
result2 = get_matrix(5, 3, 2)
result3 = get_matrix(2, 7, 22)
print(result1)
print(result2)
print(result3)