import sys
import string

words = "Apple, banana, and cherry"
words = words.lower()
words = set(words)
apha = 

print words
print len(words)


#second exercise
word1 = "This list is my first list"
word1 = word1.lower()
word1 = set(word1)

word2 = "Well, this is my second list"
word2 = word2.lower()
word2 = set(word2)

print word1
print word2

final_word1 = word1.intersection(word2)
final_word2 = word1.union(word2)

print "-------------------------------------------"
print "COmmon words are below:" 
print final_word1

print "\n" 
print "Unique words are below:"
print final_word2
print"-------------------------------------------"
