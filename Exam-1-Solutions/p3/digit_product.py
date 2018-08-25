'''
Given a  number n, find the product of all the digits
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    product = 1
    check = True
    temp = int_input
    if int_input < 0:
        check = False
        int_input = abs(int_input)
    while int_input != 0:
        product = product * (int_input % 10)
        if product == 0:
            break
        int_input = int_input // 10
    if check and temp != 0:
        print(product)
    elif temp == 0:
        print(0)
    else:
        print(-product)


if __name__ == "__main__":
    main()