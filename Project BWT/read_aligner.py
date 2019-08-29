from bwt_structures import *
from tcslib import *

def find(query, bwt_data):
    """
    Given a query sequence and a series of data structures
    containing various information about the reference genome,
    return a list containing all the locations of the query
    sequence in the reference genome. 
    """
    
    bwt, suffix_array, ranks, counts = bwt_data
      
    length = len(bwt)
    results = []
    
    """SOLUTION CODE HERE"""
    
    # Start at the end of the query.
    index = len(query)-1
    character = query[index] # Looking at the last character in the query.
    
    # Initialize the beginning and end variables, establishing
    # the subset of the sorted suffixes we are currently examining.
    new_beginning = counts[character] + 1
    new_end = counts[character] + ranks[character][-1]
    
    while index > 0: # We will backtrack through the query until we get to the beginning.
        
        old_beginning = new_beginning
        old_end = new_end
        
        character = query[index-1] # Looking at the next character in the query.
        
        # Set new beginning and end variables to reflect the new
        # subset of sorted suffixes we are currently examining.
        num_in_range = ranks[character][old_end] - ranks[character][old_beginning-1]
        new_end = counts[character] + ranks[character][old_end]
        new_beginning = new_end - num_in_range + 1
        
        # Return if we can no longer match our query to the reference
        # at any point in the backtracking process.
        if num_in_range == 0:
            return sorted(results)
        
        index = index - 1 # Continue backtracking.
        
    # Add the position(s) in the reference genome to which our
    # query aligns. This information is encoded in the suffix array.
    for i in range(new_beginning, new_end + 1):
        results.extend([suffix_array[i]])

    return sorted(results)
        
if __name__ == '__main__':
    pass
