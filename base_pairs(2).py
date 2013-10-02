sequence = 'AATTTTGGGGGGCCCCCCCC'

a = sequence.count('A')
g = sequence.count('G')
t = sequence.count('T')
c = sequence.count('C')
bp = {'A': a,'T': t,'G': g,'C':c}

print "A:" + a
print a
print t
print g
print c

#print bp['A'] print bp['T'] print bp['G'] print bp['C']

def countWord(input_string):
    d = {}
    for word in input_string:
        try:
            d[word] += 1
        except:
            d[word] = 1

    for k in d.keys():
        print "%s: %d" % (k, d[k])


print countWord("AATTTTGGGGGGCCCCCCCC")
