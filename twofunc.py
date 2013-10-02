def base_count(sequence, base):
    return sequence.count(base)

def gc_content(sequence):
    return (base_count(sequence, 'G') + 
            base_count(sequence, 'C')) / float(len(sequence))

test_data = 'GATCTAGTGATGCAC'
print "A = ",base_count(test_data,'A')
print "G = ",base_count(test_data,'G')
print "T = ",base_count(test_data,'T')
print "C = ",base_count(test_data,'C')
print "GC Content = ",gc_content(test_data)
