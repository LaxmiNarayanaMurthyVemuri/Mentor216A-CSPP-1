'''
Write a short program that prints each number from 1 to n on a new line. 
For each multiple of 3, print "Fizz" instead of the number. 
For each multiple of 5, print "Buzz" instead of the number. 
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable n.
    '''
    n = int(input())
    i=1
    while i <= n:
        if i%3 == 0:
            print("Fizz")
            if i%5 == 0:
                print("Buzz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1

if __name__ == "__main__":
    main()