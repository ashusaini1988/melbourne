from inherit import DNASequence, RNASequence
def enter_seq():
    x = ''
    while x == '':
        try:
            x = DNASequence(raw_input('Enter DNA sequence: '))
        except:
            pass
    return x
    
print enter_seq()
