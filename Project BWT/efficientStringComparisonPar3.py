# Problem 1 - Build the BWT


class SuffixArray(object):
    def __init__ (self, t):
        """ Create suffix array representing suffixes in t """
        
        self.td = t + "$"
        self.index = []  ## Array of integers representing lexicographically sorted suffixes of t
        for i in range(len(self.td)):
            self.index.append((self.td[i:], i))
        self.index.sort()
        self.index = [i[1] for i in self.index]


def makeBwt (t):
    """Create the BWT for the string t$"""
    # Code to complete
    sa = SuffixArray(t)
    transform = [sa.td[i - 1] for i in sa.index]
    return "".join(transform)


text = "GATTACA"

bwt = makeBwt(text)
print(bwt == "ACTGA$TA")


# Problem 2 - Invert the BWT

def invertBwt (bwt_string):
    """Inverts the Burrows-Wheeler Transform, returning the original string using
    inefficent algorithm"""
    bwt_loc = 0
    matrix = sorted([i for i in bwt_string])
    for x in range(len(bwt_string) - 1):
        for o in range(len(matrix)):
            matrix[o] = bwt_string[o] + matrix[o]
        matrix.sort()
    for e, loc in enumerate([i.find('$') for i in matrix]):
        if loc == len(bwt_string) - 1:
            bwt_loc = e
    return matrix[bwt_loc]


print(invertBwt(bwt) == text + "$")


# Problem 3 - Complete Last-to-First mapping using FM-index

class FmIndex(object):
    def __init__ (self, t, alphabet):
        """ Create FM-index for t in naive manner """
        
        # Make the BWT
        # We don't compress or anything here, but you could
        self.bwt = makeBwt(t)
        
        # Calculate C lookup dictionary in crappy way
        s = sorted(self.bwt)
        self.C = { }
        for i in range(len(s) - 1, -1, -1):
            self.C[s[i]] = i
        
        # Calculate full Occ table in similarly crappy way
        # Recall, this is not using sampling and is therefore
        # very memory inefficient
        self.Occ = [{ } for i in range(len(self.bwt))]
        for i in range(len(self.bwt)):
            for j in alphabet + "$":
                p = self.Occ[i - 1][j] if i > 0 else 0
                self.Occ[i][j] = p + (1 if self.bwt[i] == j else 0)
    
    def lf (self, c, i):
        """ Return the last-to-first mapping for index i of the bwt """
        return self.C[c] + self.Occ[i][c] - 1
    
    def query (self, pattern, alphabet):
        match = ''
        
        # init search range
        s = self.C[pattern[-1]] + 1
        e = self.C[alphabet[alphabet.find(pattern[-1]) + 1]]
        # get next char in alphabet to read self.C table
        
        i = 2
        match += self.bwt[self.bwt[s:e + 1].find(pattern[-1])]  # get matching char
        while pattern[-i] in self.bwt[s:e + 1]:
            s = self.lf(match[-1], s - 1) + 1
            e = self.lf(match[-1], e)
            print(self.bwt[s:e + 1])
            match += self.bwt[self.bwt[s:e + 1].find(pattern[-i])]
            i += 1
        return match


dnaAlphabet = "ACGT"
fmIndex = FmIndex(text, dnaAlphabet)

# print(fmIndex.lf(5) == 0)
#
#
# def invertBwtUsingFmIndex (fm):
#     """ Returns t by using repeated lf search to reconstruct t$ backwards"""
    # loc = fm.lf(fm.bwt.find('$'))
#     t = ''
#     for i in range(len(fm.bwt) - 1):
#         t = fm.bwt[loc] + t
#         loc = fm.lf(loc)
#     return t + '$'


# print(invertBwtUsingFmIndex(fmIndex) == "GATTACA$")

print(fmIndex.query("ATTA", "ACGT"))
