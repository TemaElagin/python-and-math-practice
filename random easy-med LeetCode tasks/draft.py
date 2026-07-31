mat = [[0, 0, 1], [1, 0, 0], [1, 1, 0]]
# transposed = [list(row) for row in zip(*mat)]
n = len(mat)
m = len(mat[0])
num_position = []
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            num_position.append([i, j])
new_num_position = []
for el in num_position:
    is_unique = 0
    for elem in num_position:
        if el[0] == elem[0] or el[1] == elem[1]:
            is_unique += 1
    if is_unique == 1:
        new_num_position.append(el)

