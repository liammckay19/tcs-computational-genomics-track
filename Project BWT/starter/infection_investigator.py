from bwt_structures import *
from read_aligner import *
from tcslib import *

def reverse_complement(seq):
    """
    Returns the reverse complement of the input string.
    """
    comp_bases = {'A': 'T',
                  'C': 'G',
                  'G': 'C',
                  'T': 'A'} 
    rev_seq = list(seq)
    rev_seq = rev_seq[::-1]
    rev_seq = [comp_bases[base] for base in rev_seq] 
    return ''.join(rev_seq)
    
def align_patient_reads():
        
    # Bacteria    
    panel = ['Bacteroides_ovatus',
             'Bacteroides_thetaiotaomicron',
             'Bifidobacterium_longum',
             'Eubacterium_rectale',
             'Lactobacillus_acidophilus',
             'Peptoniphilus_timonensis',
             'Prevotella_copri',
             'Roseburia_intestinalis',
             'Ruminococcus_bromii',
             'Vibrio_cholerae'
            ]
    
    # Patients
    patients = ['patient1',
                'patient2',
                'patient3'
               ]

    
    sequences = {}
    structures = {}


    #TODO: For each reference genome, import the DNA sequence into our "sequences"
    #       dictionary from the FASTA file located in the reference_genoms folder.
    #       REMEMBER: use the get_fasta_dict method that is imported here


    #TODO: For each reference genome, preprocess their BWT structures, storing each
    #       one in the "structures" dictionary
    #       HINT: the make_all method that is imported should help



    reads = {}

    #TODO: for each patient, import their reads into the "reads" dictionary
    #       where keys are the patient IDs and the values are another dictionary
    #       containing pairs of read ID : read
    


    #TODO: begin iterating through each read for each patient, collecting all 
    #       necessary data for later analysis... this involves
    #           * classifying each read (identifying the microbe)
    #           * counting the prevalence of each microbe in each patient
    #
    #           ** don't forget to call reverse_complement on reads **
    #           ** don't forget to discard reads that map to more than one microbe **





    #TODO: store the data you collect somewhere, either printing out the prevalences
    #       and copy/pasting them, or writing directly to a txt file
       


    #TODO: analyze your data and refelct -- go back to project instructions



if __name__ == '__main__':
    align_patient_reads()
