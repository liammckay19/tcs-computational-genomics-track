from tcslib import *   # this will also import the sys and re modules
import re
import random

#returns a list of dictionaries 
def find_orfs(sequence, minLength):

    '''
    Your code goes here
    '''
       
    # TODO: returns list of ORFS formatted as
      #[ {’frame’: 0, ’stop’: 13413, ’aalength’: 4382, ’start’: 265,’stopcodon’: ’UAA’, ’nlength’: 13149}, {}, {} ]
                                
                
    return

#main function
def solve_orfs():
    
    #string of sequence found with sequenceDictionary["sars"]
    sequenceDictionary = get_fasta_dict("sars.fasta") 
    
    

    """Your code goes here..."""



    # TODO: print number of ORFs found, given minimum ORF length

    # TODO: print the mean peptide length of ORFs


 
    # TODO: simulate mutations
      
        
if __name__ == '__main__':
    solve_orfs()
