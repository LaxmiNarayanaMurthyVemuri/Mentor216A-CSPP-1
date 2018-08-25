'''
Sudoku is a logic-based, combinatorial number-placement puzzle.
The objective is to fill a 9×9 grid with digits so that
each column, each row, and each of the nine 3×3 subgrids that compose the grid
contains all of the digits from 1 to 9.

Complete the check_sudoku function to check if the given grid
satisfies all the sudoku rules given in the statement above.
'''
def is_valid_cells(sudoku, length):
    '''
    Only checking rows and columns duplicates and values in range[1,9]
    '''
    for row in sudoku:
        if len(set(row)) != length:
            return False
        for element in row:
            if element not in [number for number in range(1, 10)]:
                return False
    return True

def check_sudoku(sudoku):
    '''
    validating sudoku
    '''
    return is_valid_cells(sudoku, len(sudoku)) and is_valid_cells(zip(*sudoku), len(sudoku))

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
