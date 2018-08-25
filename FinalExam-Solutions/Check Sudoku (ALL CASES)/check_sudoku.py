'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

from math import sqrt
def _is_valid_row(row_num, len_sudoku, sudoku):
    return _is_valid_set(set(sudoku[row_num]), len_sudoku)

def _is_valid_column(column_num, len_sudoku, sudoku):
    return _is_valid_set(set([sudoku[r][column_num] for r in range(len_sudoku)]), len_sudoku)

def _is_valid_block(block_num, block_len, len_sudoku, sudoku):
    block_row_num, block_column_num = divmod(block_num, block_len)
    block_row, block_column = block_row_num * block_len, block_column_num * block_len
    block_set = set()
    for row in range(block_row, block_row + block_len):
        for column in range(block_column, block_column + block_len):
            block_set.add(sudoku[row][column])
    return _is_valid_set(block_set, len_sudoku)

def _is_valid_set(num_set, len_sudoku):
    return len(num_set) == len_sudoku \
           and max(num_set) == len_sudoku \
           and min(num_set) == 1


def check_sudoku(sudoku):
    '''
    driver Function
    '''
    len_sudoku = len(sudoku)
    try:
        block_len = int(sqrt(len_sudoku))
    except ValueError:
        return False
    if any([len(row) != len_sudoku for row in sudoku]):
        return False
    return all([_is_valid_row(i, len_sudoku, sudoku)
                and _is_valid_column(i, len_sudoku, sudoku)
                and _is_valid_block(i, block_len, len_sudoku, sudoku)
                for i in range(len_sudoku)])

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append([int(element) for element in row])
    # call solution function and print result to console
    print(check_sudoku(sudoku))
    # print(sudoku)

if __name__ == '__main__':
    main()
