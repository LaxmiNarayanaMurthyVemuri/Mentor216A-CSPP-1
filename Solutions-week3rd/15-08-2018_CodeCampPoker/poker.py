'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
GLOBAL_DICT = {
    '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14
}

def get_face_hand(hand):
    '''
    getting face values of hand
    '''
    face_hand = [r for r, s in hand]
    return face_hand

def get_suit_hand(hand):
    '''
    getting face values of hand
    '''
    suit_hand = [s for r, s in hand]
    return suit_hand

def is_four_a_kind(hand):
    '''
    is_four_a_kind
    '''
    face_hand = get_face_hand(hand)
    for i in face_hand:
        if face_hand.count(i) == 4:
            return True
    return False

def is_full_house(hand):
    '''
    is_full_house
    '''
    face_hand = get_face_hand(hand)
    if is_three_a_kind(hand) and len(set(face_hand)) == 2:
        return True
    return False

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False.
        Return True if all the cards have the same suit.
    '''
    suit_hand = get_suit_hand(hand)
    return len(set(suit_hand)) == 1

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
        Return True if the ordered ranks form a 5-card straight."
    '''
    rank = []
    for card in hand:
        rank.append(GLOBAL_DICT[card[0]])
    return sum(rank) - min(rank)*5 == 10

def is_three_a_kind(hand):
    '''
    is_three_a_kind
    '''
    face_hand = get_face_hand(hand)
    face_hand.sort()
    status = False
    for i in face_hand:
        if face_hand.count(i) >= 3:
            status = True
            break
    return status

def is_two_pair(hand):
    '''
    is_two_pair
    '''
    face_hand = get_face_hand(hand)
    if not is_three_a_kind(hand) and len(set(face_hand)) == 3:
        return True
    return False

def is_one_pair(hand):
    '''
    is_one_pair
    '''
    face_hand = get_face_hand(hand)
    return len(set(face_hand)) == 4

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush
    if is_straight(hand) and is_flush(hand):
        #print("straight flush")
        return 8
    elif is_four_a_kind(hand):
        #print("four kind")
        return 7
    elif is_full_house(hand):
        #print("Full house")
        return 6
    elif is_flush(hand):
        #print("Flush")
        return 5
    elif is_straight(hand):
        #print("Staright")
        return 4
    elif is_three_a_kind(hand):
        #print("Three Kind")
        return 3
    elif is_two_pair(hand):
        #print("Two pair")
        return 2
    elif is_one_pair(hand):
        #print("One pair")
        return 1
    return 0
    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand


def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input().replace('\r', '')
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
