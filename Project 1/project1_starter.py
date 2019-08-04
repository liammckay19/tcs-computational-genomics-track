from tcslib import * 
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



def main():
    
    sequenceDictionary = get_fasta_dict("sars.fasta") 
    sarsSequence = sequenceDictionary["sars"]


    
    '''
    Your code goes here
    '''



    # TODO: print number of ORFs found, given minimum ORF length

    # TODO: print the mean peptide length of ORFs


 
    # TODO: /Section 2/ simulate mutations (hint: create additional methods)
      


        
if __name__ == '__main__':
    main()
