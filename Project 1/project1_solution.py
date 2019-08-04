from tcslib import *   # this will also import the sys and re modules
import re
import random

def random_amino_acid (old):
    '''
    Given an amino acid, this function will return a random, different amino acid
    '''
    aalist = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"] 
    new=old  
    while new == old:
        new = aalist[random.randint(0,19)]
    
    return new

def random_nucleotide (old):
    '''
    Given a nucleotide, this function will return a random, different RNA nucleotide
    '''
    nuclist = ["a", "c", "u", "g"] 
    new=old  
    while new == old:
        new = nuclist[random.randint(0,3)]
    
    return new   

def find_orfs(seq, min):
    '''
    This function searches the three reading frames of a single stranded sequence to find all open reading frames
    of a minimum codon length.
    '''


    #making frameshift codon arrays
    codons0 = re.findall('...', seq)
    codons1 = re.findall('...', seq[1:]) 
    codons2 = re.findall('...', seq[2:]) 
    
    
    myORFs = []

    '''
    The following long section of code is repetitive, with three code blocks (one for each frame) They are only different
    in their nucleotide position offsets due to frame shifting
    '''

    index=0
    while index<len(codons0):
        if codons0[index]=="aug":
            startnuc = (index *3) +1

            for y in range(index, len(codons0)):
                if codons0[y]=="uag" or codons0[y]=="uga" or codons0[y]=="uaa":
                    stopnuc=(y*3) + 3
                    stopcodon= codons0[y]
                    nuclength = (stopnuc - startnuc) +1
                    peplength = (nuclength/3) -1

                    if peplength<min:
                        index=y
                        break

                    index=y
                    myORFs.append({"frame":0, "stop": stopnuc, "aalength":peplength, "start":startnuc, "stopcodon":stopcodon, "nlength":nuclength})
                    break
        index+=1

    index=0
    while index<len(codons1):
        if codons1[index]=="aug":
            startnuc = (index *3) +2

            for y in range(index, len(codons1)):
                if codons1[y]=="uag" or codons1[y]=="uga" or codons1[y]=="uaa":
                    stopnuc=(y*3) + 4
                    stopcodon= codons1[y]
                    nuclength = (stopnuc - startnuc) +1
                    peplength = (nuclength/3) -1

                    if peplength<min:
                        index=y
                        break

                    index=y
                    myORFs.append({"frame":1, "stop": stopnuc, "aalength":peplength, "start":startnuc, "stopcodon":stopcodon, "nlength":nuclength})
                    break
        index+=1
                
    index=0
    while index<len(codons2):
        if codons2[index]=="aug":
            startnuc = (index *3) +3

            for y in range(index, len(codons2)):
                if codons2[y]=="uag" or codons2[y]=="uga" or codons2[y]=="uaa":
                    stopnuc=(y*3) + 5
                    stopcodon= codons2[y]
                    nuclength = (stopnuc - startnuc) +1
                    peplength = (nuclength/3) -1

                    if peplength<min:
                        index=y
                        break

                    index=y
                    myORFs.append({"frame":2, "stop": stopnuc, "aalength":peplength, "start":startnuc, "stopcodon":stopcodon, "nlength":nuclength})
                    break
        index+=1       
                                   
                
    return myORFs

def main():
    """Your code goes here..."""
    sequenceDictionary = get_fasta_dict("sars.fasta")
    
    minLengths = [10,50,70]

    for length in minLengths:
        ORFs = find_orfs(sequenceDictionary["sars"],length)
        print "Our algorithm has found " + str(len(ORFs)) + " ORFs longer than " + str(length) + " amino acids"        
        
        #finding and printing the mean of all the peptide lengths
        total =0
        for dictionary in ORFs:
            total = total + float(dictionary["aalength"])
        
        mean = total/len(ORFs)
        print "The mean peptide length is: " + str(mean) + "\n"
 


    #getting data from the fourth ORF of minimum 10 for mutation use
    ORFs = find_orfs(sequenceDictionary["sars"],10)

    fourthORF= sequenceDictionary["sars"][ORFs[3]["start"]-1:ORFs[3]["stop"]]
    translatedORF = translate(fourthORF)[:-1]
    
    
    print "\nsingle nucleotide changes"
    print translate(fourthORF)
    for i in range(10):
        randnucnum= random.randint(0,len(fourthORF)-1)
        newnuc = random_nucleotide(fourthORF[randnucnum])
        newseq = fourthORF[0:randnucnum] + newnuc + fourthORF[randnucnum+1:]
        fourthORF =  newseq
        
        print translate(fourthORF)

    print "\n\nsingle AA changes"
    print translatedORF
    for z in range(10):
        randaanum= random.randint(0,len(translatedORF)-1)
        newaa = random_amino_acid(translatedORF[randaanum])
        newtranslate = translatedORF[0:randaanum] + newaa + translatedORF[randaanum+1:]
        translatedORF =  newtranslate
        
        print translatedORF
       z
        
if __name__ == '__main__':
    main()
