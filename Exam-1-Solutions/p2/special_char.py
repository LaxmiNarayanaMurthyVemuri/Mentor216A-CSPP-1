'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has four spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read any string from the input, store it in variable str_input.
    '''
    str_input = input()
    new_string = ""
    if len(str_input) != 0:
        for i in range(len(str_input)):
            if str_input[i] in "!@#$%^&*":
                new_string = new_string + " "
            else:
                new_string = new_string + str_input[i]
        print(new_string)
    else:
        print()

if __name__ == "__main__":
    main()