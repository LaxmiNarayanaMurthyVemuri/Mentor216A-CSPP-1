def mult_matrix(matrix_one, matrix_two):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    rows = len(matrix_one)
    columns = len(matrix_two[0])
    multi_matrix = generate_resultant_matrix(rows, columns)
    if len(matrix_one[0]) == len(matrix_two):
        pass
    else:
        print("Error: Matrix shapes invalid for mult")
        return None


def generate_resultant_matrix(rows, columns):
    add_matrix = []
    for j in range(rows):
        add_matrix.append([])
        for i in range(columns):
            add_matrix[j].append(0)
    return add_matrix


def add_matrix(matrix_one, matrix_two):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    rows = len(matrix_one)
    columns = len(matrix_one[0])
    add_matrix = generate_resultant_matrix(rows, columns)
    if len(matrix_one[0]) == len(matrix_two[0]):
        for i in range(rows):
            for j in range(columns):
                add_matrix[i][j] += matrix_one[i][j] + matrix_two[i][j]
        return add_matrix
    else:
        print("Error: Matrix shapes invalid for addition")
        return None


def read_matrix():
    ''' 
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    list_input = input().split(',')
    rows, columns = int(list_input[0]), int(list_input[1])
    for _ in range(rows):
        list_matrix_row = input().split()
        if columns == len(list_matrix_row):
            matrix.append([int(i) for i in list_matrix_row])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix



def main():
    # read matrix 1
    matrix_one = read_matrix()
    if matrix_one is None:
        exit()
    
    # read matrix 2
    matrix_two = read_matrix()
    if matrix_two is None:
        exit()

    # add matrix 1 and matrix 2
    print(add_matrix(matrix_one, matrix_two))
    # multiply matrix 1 and matrix 2
    print(mult_matrix(matrix_one, matrix_two))
if __name__ == '__main__':
    main()
