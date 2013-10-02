#Create a class DNASequence



class DNASequence:
    def __init__(self,sequence):
        self.sequence = sequence
    
    def base_count(self, base):
        return self.sequence.count(base)
    
    def gc_content(self):
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)

    def reverse_complement(self):
        #rev = self.sequence[::-1]
        complements =   {'G':'C',
                        'C': 'G',
                        'A': 'T',
                        'T': 'A'}
        rev_c = ""
        for base in self.sequence:
            rev_c = complements[base] + rev_c
            
        return rev_c
