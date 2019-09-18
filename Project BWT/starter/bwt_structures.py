from collections import Counter
from tcslib import *

# Note that the '$' character will be used to designate the end of a given string.

def forward_bwt(seq):
    """
    forward_bwt(seq) takes as input a string containing the EOF
    character to which the BWT must be applied. The method should
    then return the result of the BWT on the input string.
    
    For example:
    print forward_bwt('GATTACA$') --> 'ACTGA$TA'
    """
    
    # TODO: Add code to create bwt
    # Return the last column from the sorted list of rotations.
    
    # Hint: You are given this piece of code below that will return the last character in 
    #       an string array of rotations. 
    return "".join(x[-1] for x in sorted(rotations))
    

# It may be helpful to read the documentation for the methods
# given below, but you will NOT have to make any changes to
# them in order to complete the problems

def make_suffix_array(seq):
    """
    Returns the suffix array of the input string.
    
    For example:
    print make_suffix_array('GATTACA$') --> [7, 6, 4, 1, 5, 0, 3, 2]
    
    because this is the order in lexographical order:
    7 $GATTACA
    6 A$GATTAC
    4 ACA$GATT
    1 ATTACA$G
    5 CA$GATTA
    0 GATTACA$
    3 TACA$GAT
    2 TTACA$GA
    """
    suffixes = {}
    # TODO: Populate the suffix array. 
    # This is the array that will order every suffix or rotation and display the index position of the rotation. 
    return suffix_array

def occ_rank(bwt_seq):
    """
    Takes as input a string transformed by the BWT. Returns a
    dictionary with characters as keys and lists as values.
    Each list contains the total number of occurrences for the 
    corresponding character up until each position in the
    BWT-transformed string (i.e., its rank).
    
    For example:
    print rank('ACTGA$TA')['$'] --> [0, 0, 0, 0, 0, 1, 1, 1]
    print rank('ACTGA$TA')['A'] --> [1, 1, 1, 1, 2, 2, 2, 3]
    print rank('ACTGA$TA')['C'] --> [0, 1, 1, 1, 1, 1, 1, 1]
    print rank('ACTGA$TA')['G'] --> [0, 0, 0, 1, 1, 1, 1, 1]
    print rank('ACTGA$TA')['T'] --> [0, 0, 1, 1, 1, 1, 2, 2]
    """
    rank = {}
    characters = set(bwt_seq)
    # (You may give the answer to the student) TODO: Populate the Occ table for occurences of letters
    return rank

def count_smaller_chars(seq):
    """
    Takes as input a string. Returns a dictionary with characters
    as keys and integers as values. The integers track the
    number of characters in the input string which are
    lexicographically smaller than the corresponding character
    key.
    
    For example, using an input DNA sequence like 'GATTACA':
    print count_smaller_chars('GATTACA')['A'] --> 0  (A, being lexicographically first, should always return 0)
    print count_smaller_chars('GATTACA')['C'] --> 3  (C, being second, should return the number of A's, which is 3)
    print count_smaller_chars('GATTACA')['G'] --> 4  (G, being third, should return the number of A's or C's, which is 4)
    print count_smaller_chars('GATTACA')['T'] --> 5  (T, being fourth, should return the number of A's or C's or G's, which is 5)
    """
    characters = set(seq)
    cntr = Counter(seq)
    total = 0
    counts = {}
    # TODO: Count the smaller characters per character 
    return counts

def make_all(reference):
    """
    Takes as input a reference string. Returns the data
    structures necessary to perform efficient exact string
    matching searches.
    """
    counts = count_smaller_chars(reference)
    reference = reference + '$'
    suffix_array = make_suffix_array(reference)
    bwt = forward_bwt(reference)
    ranks = occ_rank(bwt)
    return bwt, suffix_array, ranks, counts

if __name__ == '__main__':
    pass
