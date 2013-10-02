seq1 = 'AGGGTTTTCCCAAAATTTTTTTTTTTTTTTGGGGGGGGG'
is_new = False
if 'U' in seq1:
    is_new = True
seq1 = seq1.replace('U','T')

a = seq1.count('A')
g = seq1.count('G')
t = seq1.count('T')
c = seq1.count('C')

bp = {'A': a,'T': t,'G': g,'C': c}
print bp

total_length = g+a+t+c
gc_content = (g+c)/float(total_length) * 100
bp['U'] = bp['T']
del bp['T']
print gc_content
print bp



