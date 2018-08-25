'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    '''
    TOKENIZE
    '''
    dictionary = {}
    for i in string:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    return dictionary

def clean_string(text):
    '''
    CLEAN STRING
    '''
    return re.sub('[^a-zA-Z0-9]', " ", text.replace('\'', ''))

def main():
    '''
    MAIN
    '''
    sample_string = ""
    for _ in range(int(input())):
        sample_string += clean_string(input())
    print(tokenize(sample_string.split()))

if __name__ == '__main__':
    main()
