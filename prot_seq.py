reader = open('uniprot_sprot.fasta', 'r')
line = reader.readline()
noOfHumanProteins=0
for line in reader:
    if ( line[0] == '>'):
        if "Homo sapiens" in line:
            noOfHumanProteins+=1
        print "No = ",noOfHumanProteins
f.close()
