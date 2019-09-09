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
    
    """SOLUTION CODE HERE"""
    rotations = []
    
    # Generate list of rotations.
    for x in range(len(seq)):
        new_s = seq[x:] + seq[:x]
        rotations.append(new_s)
        
    # Return the last column from the sorted list of rotations.
    return "".join(x[-1] for x in sorted(rotations))
    
def reverse_bwt(seq):
    """
    reverse_bwt(seq) takes as input a string containing the EOF
    character to which the reverse of the BWT must be applied.
    The method should then return the result of the reversal on
    the input string.
    
    For example:
    print reverse_bwt('ACTGA$TA') --> 'GATTACA$'
    """    
    
    """SOLUTION CODE HERE"""
    
    # This solution employs an implementation of the
    # LF mapping strategy outlined in Problem 3 Part (b).
    # Commented out below is a solution which relies on
    # an append-and-sort strategy. Both are valid ways to
    # solve the problem at hand.
    
    # LF MAPPING STRATEGY
    '''
    firstColumnChars = ''.join(sorted(list(seq)))
    firstColumnRanks = rank(firstColumnChars)

    lastColumnRanks = rank(seq)
    
    originalSequence = ""
    currentPosition = lastColumnRanks["$"].index(1)
    while currentPosition != 0:
        currentChar = firstColumnChars[currentPosition]
        originalSequence += currentChar
        nextPosition = firstColumnRanks[currentChar][currentPosition]
        currentPosition = lastColumnRanks[currentChar].index(nextPosition)
    
    originalSequence += "$"
    
    return originalSequence
    '''
    # APPEND-AND-SORT STRATEGY
    
    # Initialize empty table.
    rotations = [[] for x in range(len(seq))]
    
    # Repeat for as many characters as there are in the input sequence.
    counter = 0
    while counter < len(seq):
        counter += 1
        
        # Insert sequence as first column of the table.
        for x in range(len(rotations)):
            rotations[x].insert(0,seq[x])
            
        # Sort rows of the table alphabetically.
        rotations.sort()
    
    # Return rotation ending in '$' (i.e. the original sequence).
    for x in range(len(rotations)):
        if rotations[x][-1] == '$':
            return "".join(rotations[x])
    return "No EOF character ('$') found."
    

# It may be helpful to read the documentation for the methods
# given below, but you will NOT have to make any changes to
# them in order to complete the problem set.

def make_suffix_array(seq):
    """
    Returns the suffix array of the input string.
    
    For example:
    print make_suffix_array('GATTACA$') --> [7, 6, 4, 1, 5, 0, 3, 2]
    """
    suffixes = {}
    for x in range(len(seq)):
        suffixes[seq[x:]] = x
    suffix_array = [suffixes[suffix] for suffix in sorted(suffixes.keys())]
    return suffix_array

def rank(bwt_seq):
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
    for character in characters:
        rank[character] = [0]
    rank[bwt_seq[0]] = [1]
    for letter in bwt_seq[1:]:
        for k, v in rank.items():
            v.append(v[-1] + (k == letter))
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
    for character in sorted(characters):
        counts[character] = total
        total += cntr[character]
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
    ranks = rank(bwt)
    return bwt, suffix_array, ranks, counts

if __name__ == '__main__':
    pass
