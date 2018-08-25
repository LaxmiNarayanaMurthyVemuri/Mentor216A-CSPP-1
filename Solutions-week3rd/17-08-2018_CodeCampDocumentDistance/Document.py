'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
from collections import Counter

def text_to_vector(text):
    '''
        modifying text to vector by cleaning, by using re module
    '''
    word = re.compile(r'\w+')
    words = word.findall(text)
    stopwords = set(load_stopwords("stopwords.txt"))
    words = [word for word in words if word not in stopwords]
    return Counter(words)

def get_cosine(vec1, vec2):
    '''
        apply cosine formula.
    '''
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    return numerator / denominator

def similarity(input1, input2):
    '''
        Compute the document distance as given in the PDF
    '''
    vector1 = text_to_vector(input1.lower())
    vector2 = text_to_vector(input2.lower())
    return get_cosine(vector1, vector2)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
