import splitter_nltk
from nltk.tokenize import word_tokenize
import sys 

reload(sys)  
sys.setdefaultencoding('utf8')

name = raw_input("Give words file name: ")
name = name + '.txt'

try:
	words = sorted(open(name, 'r').readlines())
except IOError:
	print "File does not exist"

sentences = splitter_nltk.sentences

def binary_search(words, word):
	if len(words) == 0:
		return False
	else:
		midpoint = len(words)//2
		checkWord = (words[midpoint])[:-1]
		if checkWord == word:
			return True
		else:
			if word < checkWord:
				return binary_search(words[:midpoint], word)
			else:
				return binary_search(words[midpoint+1:], word)

word_sentences = [[]]


def fill_object(sentences, words):
	for sentence in sentences:
		sentence_split = word_tokenize(sentence)
		for word in sentence_split:
			if word == '.': #A dot is treated as a word since that's needed to indicate the end of a sentence
				continue
			if (binary_search(words, word) == True):
				print sentence, word

fill_object(sentences, words)



