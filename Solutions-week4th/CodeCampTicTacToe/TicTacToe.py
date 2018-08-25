'''
To verify the winner for the TicTocToe Game
@author : Murthy Vemuri
'''
ROWS = 3
COLUMNS = 3

def is_valid_input(matrix):
    '''
    To check if the input is a valid input
    '''
    for row in matrix:
        for element in row:
            if element not in 'x.o':
                return False
    return True

def is_valid_game(new_test):
    '''
    to check if it is a valid game
    '''
    count_x_variable = 0
    count_o_variable = 0
    for row in new_test:
        count_x_variable += row.count('x')
        count_o_variable += row.count('o')
    if count_x_variable > 5 or count_o_variable > 5 or count_x_variable == count_o_variable:
        print("invalid game")
        return None
    return True

def is_verification_rows_columns(matrix, check_variable):
    '''
    To verify all the rows, columns values are 'x and 'o'
    '''
    for row in matrix:
        if row[0] == check_variable and len(set(row)) == 1:
            return True
    return False

def is_winner(matrix, check_variable):
    '''
    To check whether variable 'x' or 'o' is present
    '''
    flip_matrix = zip(*matrix)
    if is_verification_rows_columns(flip_matrix, check_variable) or\
        is_verification_rows_columns(matrix, check_variable):
        return True
    elif (matrix[0][0] == matrix[1][1] == matrix[2][2] == check_variable) or\
        (matrix[0][2] == matrix[1][1] == matrix[2][0] == check_variable):
        return True
    else:
        return False

def reading_testcases():
    n = int(input())
    for _ in range(n):
        string_dummy = input()
        tictactoe = input_reading()
        main_(tictactoe)

def input_reading():
    tictactoe = []
    for _ in range(ROWS):
        tictactoe.append(input().strip().split())
    return tictactoe

def main():
    '''
    Main function
    '''
    tictactoe = input_reading()
    if is_valid_input(tictactoe):
        if is_valid_game(tictactoe):
            if is_winner(tictactoe, 'x'):
                print('x')
            elif is_winner(tictactoe, 'o'):
                print('o')
            else:
                print('draw')
    else:
        print("invalid input")

# reading_testcases()
main()
