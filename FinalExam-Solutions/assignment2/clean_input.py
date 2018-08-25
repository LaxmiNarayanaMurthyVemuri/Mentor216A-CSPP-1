'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(text):
    '''
    CLEAN STRING
    '''
    return re.sub('[^a-zA-Z0-9]', "", text.replace('\'', ''))
def main():
    '''
    MAIN
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
