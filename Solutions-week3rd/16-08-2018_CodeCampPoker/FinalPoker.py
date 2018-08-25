'''
-----------
User Instructions

Modify the hand_rank function so that it returns the
correct output for the remaining hand types, which are:
full house, flush, straight, three of a kind, two pair,
pair, and high card hands.

Do this by completing each return statement below.
You may assume the following behavior of each function:
straight(ranks): returns True if the hand is a straight.
flush(hand):     returns True if the hand is a flush.
kind(n, ranks):  returns the first rank that the hand has
exactly n of. For A hand with 4 sevens
this function would return 7.
two_pair(ranks): if there is a two pair, this function
returns their corresponding ranks as a
tuple. For example, a hand with 2 twos
and 2 fours would cause this function
to return (4, 2).
card_ranks(hand) returns an ORDERED tuple of the ranks
in a hand (where the order goes from
highest to lowest rank).
Since we are assuming that some functions are already
written, this code will not RUN. Clicking SUBMIT will
tell you if you are correct.
'''
def hand_rank(hand):
    '''
    You will code this function. The goal of the function is to
    return a value that max can use to identify the best hand.
    As this function is complex we will progressively develop it.
    The first version should identify if the given hand is a straight
    or a flush or a straight flush.
    '''
    return_value = None
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return_value = (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return_value = (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return_value = (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return_value = (5, ranks)
    elif straight(ranks):                          # straight
        return_value = (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return_value = (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return_value = (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return_value = (1, kind(2, ranks), ranks)
    else:                                          # high card
        return_value = (0, ranks)
    return return_value

def card_ranks(cards):
    '''
    Return a list of the ranks,sorted with higher first
    '''
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return ranks

def straight(ranks):
    '''
    Return True if the ordered ranks from a 5-card straight
    '''
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    '''
    Return True if all the cards have the same suit
    '''
    suits = [s for r, s in hand]
    return len(set(suits)) == 1

def kind(count, ranks):
    '''
    Return all three kind, four kind, one pair.
    '''
    for rank in ranks:
        if ranks.count(rank) == count:
            return rank
    return None

def two_pair(ranks):
    '''
    Return a list of the ranks for two pairs.
    '''
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

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
        hand_list = line.split(" ")
        HANDS.append(hand_list)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
