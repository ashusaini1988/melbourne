import sys

a = int(sys.argv[1])

if (a<50) and (a>0):
    print "Minor"
    
elif (a>=50) and (a <1000):
    print "Major"

else:
    print "severe"
