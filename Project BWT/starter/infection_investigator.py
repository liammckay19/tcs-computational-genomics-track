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
    
    """SOLUTION CODE HERE"""
    
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
    for bacteria in panel:
        # For each of the bacteria in our panel, create a dictionary entry
        # where keys are bacterial names and values are their genome sequences.
        sequences[bacteria] = get_fasta_dict('reference_genomes/%s.fasta' % bacteria).values()[0]

        # For each of the bacterial genome sequences, create a dictionary entry
        # where keys are bacterial names and values are their BWT data structures.
        structures[bacteria] = make_all(sequences[bacteria])

    reads = {}
    for x in range(1,4):
        # For each of the patients, create a dictionary entry
        # where keys are patient IDs and values are dictionaries containing read ID:read pairs
        reads['patient%d' % x] = get_fasta_dict('patients/patient%d.fasta' % x)
    
    # Initialize numbers in order to calculate percentage of reads completed.
    counter = 0
    total_reads = float(100000) * len(patients)
    
    # Consider all patients.
    for patient in patients:
        counts = {}
        
        # Consider all reads.
        for read in reads[patient]:
            
            # Update the percentage.
            counter += 1
            per_cent = (counter/total_reads)*100
            print 'You are %.4f percent finished.' % per_cent
            
            # Consider all bacteria.
            bact_list = []
            for bacteria in panel:
                # Map the reverse complement to the given bacterial reference genome.
                found = find(reverse_complement(reads[patient][read]), structures[bacteria])
                if len(found) > 0:
                    bact_list.append(bacteria)
                    if bacteria in counts.keys():
                        counts[bacteria].extend(found)
                    else:
                        counts[bacteria] = []
                        counts[bacteria].extend(found)
            # If read in more than one genome, remove from mapping.
            if len(bact_list) > 1:
                for bact in bact_list:
                    for count in find(reverse_complement(reads[patient][read]), structures[bact]):
                        counts[bact].remove(count)
                       
        # Write prevalence data to files. 
        f = open('%s_counts.txt' % patient, 'w')
        for bacteria in sorted(counts.keys()):
            f.write(bacteria + '*')
            f.write('%.4f*' % (len(counts[bacteria])/(total_reads/len(patients))))
            f.write(str(sorted(counts[bacteria])) + '\n')
        f.close()
    
    # Call to functions which generate a given vector count and
    # locate the longest string of zeros in such a vector.
    patient1_Vc_counts = read_mapper('patient1', 'Vibrio_cholerae')
    patient3_Vc_counts = read_mapper('patient3', 'Vibrio_cholerae')
    
    long0s_patient1 = longest_zeros(patient1_Vc_counts)
    long0s_patient3 = longest_zeros(patient3_Vc_counts)
    print '\nThe longest string of zeros for patient 1 is between indices %s and %s.' % (long0s_patient1[0], long0s_patient1[1])
    print 'This corresponds to the nucleotide sequence: %s' % sequences['Vibrio_cholerae'][long0s_patient1[0]:long0s_patient1[1]+1]
    print 'There is no internal string of zeros for patient 3.'

    
def read_mapper(patient, bacteria):
    # For a given patient and bacterial species, return a vector
    # which counts the number of the patient's reads which map
    # to each of the locations in the reference genome for the
    # bacterial species.
    
    f = open('%s_counts.txt' % patient, 'r')
    lines = f.readlines()
    starting_pos = [int(x) for x in ([x.split('*') for x in lines if x.startswith(bacteria)][0][2][1:-2].split(', '))]
    all_pos = []
    for pos in starting_pos:
        all_pos.extend(range(pos,pos+50))

    genome = get_fasta_dict('reference_genomes/%s.fasta' % bacteria).values()[0]
    
    count_vector = [0 for x in range(0,len(genome))]
    for pos in all_pos:
        count_vector[pos] += 1
    
    return count_vector

def longest_zeros(count_vector):
    # Given a count vector, return the start and stop position of
    # the longest string of zeros in the vector.
    
    zero_nums = []
    for i in range(0,len(count_vector)):
        if count_vector[i] == 0:
            zero_nums.append(i)
            
    counter = 1
    longest_run = {}
    longest_run[1] = []
    longest_run[1].append(zero_nums[0])
    for z in zero_nums[1:]:
        if (z - longest_run[counter][-1]) == 1:
            longest_run[counter].append(z)
        else:
            counter += 1
            longest_run[counter] = []
            longest_run[counter].append(z)
            
    for run in longest_run.keys():
        if 0 in longest_run[run] or 14999 in longest_run[run]:
            del longest_run[run]
            
    longest = []
    for run in longest_run.values():
        if len(run) > len(longest):
            longest = run
    
    if len(longest) == 0:
        return None 
    
    start = longest[0]
    stop = longest[-1]

    return start, stop

if __name__ == '__main__':
    align_patient_reads()
