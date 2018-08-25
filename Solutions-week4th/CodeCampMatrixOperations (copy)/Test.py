def generate_resultant_matrix(rows, columns):
    add_matrix = []
    for j in range(rows):
        add_matrix.append([])
        for i in range(columns):
            add_matrix[j].append(0)
    return add_matrix
rows = 6
columns = 3
add_matrix = generate_resultant_matrix(rows, columns)
add_matrix[0][2] += 2
print(add_matrix)