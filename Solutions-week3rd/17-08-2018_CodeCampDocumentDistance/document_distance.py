'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math


def clean_text(text):
    regex = re.compile('[^a-z]')
    words = text.lower().split(" ")
    return [regex.sub('', word.strip()) for word in words]

def vectorize(dictionary, words, index):
    stopwords = load_stopwords("stopwords.txt")
    for word in words:
        if word not in stopwords and len(word) > 0:
            if word not in dictionary:
                dictionary[word] = [0, 0]
            dictionary[word][index] += 1
    return dictionary

def compute_distance(dictionary):
    numerator = sum([k[0] * k[1] for k in dictionary.values()])
    d1 = math.sqrt(sum([k[0] ** 2  for k in dictionary.values()]))
    d2 = math.sqrt(sum([k[1] ** 2  for k in dictionary.values()]))
    return numerator/(d1*d2)



def similarity(input1, input2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary = {}
    dictionary = vectorize(dictionary, clean_text(input1), 0)
    dictionary = vectorize(dictionary, clean_text(input2), 1)
    return compute_distance(dictionary)

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
