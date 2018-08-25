'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    main function
    '''
    n_lines = int(input())
    for _ in range(n_lines):
        print(input())

if __name__ == '__main__':
    main()
