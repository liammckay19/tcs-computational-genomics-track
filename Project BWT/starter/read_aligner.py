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
    # TODO: Add code for the beginning of the algorithm
    while index > 0: # We will backtrack through the query until we get to the beginning.
        # TODO: Complete the algorithm for the query
        
    # Add the position(s) in the reference genome to which our
    # query aligns. This information is encoded in the suffix array.
    for i in range(new_beginning, new_end + 1):
        results.extend([suffix_array[i]])

    return sorted(results)
        
if __name__ == '__main__':
    pass
