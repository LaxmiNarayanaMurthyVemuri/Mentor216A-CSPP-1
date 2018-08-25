'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    # remove the pass below and start writing your code
    network = {}
    #print(data)
    #Please do check the output of the data variable
    #which is a parameter of this function.
    elements = data.splitlines()
    #This is split data by new lines (\n) where each and every line
    #is updated in the elements list.
    for element in elements:
        line = element.split(" follows ")
        #print(line)
        #Every line has string " follows " I have given space before and
        # follows word because every line has the same structure.
        if line[0] not in network:
            if len(line) != 1:
                #This condition helps me in passing third test case.
                network[line[0]] = line[1].split(",")
                #To update the values by splitting with comma, I am updating
                #dictionary.
    return network
    #Finally returing network dictionary.

def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
