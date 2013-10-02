seq1 = 'AGGGTTTTCCCAAAATTTTTTTTTTTTTTTGGGGGGGGG"
is_new = FALSE
if 'U' in seq1:
    is_new = TRUE
seq1 = seq.replace('U','T')

a = seq1.count('A')
g = seq1.count('G')
t = seq1.count('T')
c = seq1.count('C')

bp = {'A:' a,"T: " t,"G: " g,"C: " c}
print bp
