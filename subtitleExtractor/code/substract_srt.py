import pysrt
import sys


#name = raw_input("Give subtitle file name: ")
#name = name + '.srt'

name = 'The Shawshank Redemption (1994) 720p BrRip x264 [Dual Audio] [Hindi-English]-LokiST [Silve.srt'

try:
	subs = pysrt.open(name)
except UnicodeDecodeError:
	subs = pysrt.open(name, encoding='iso-8859-1')
except IOError:
	print "File does not exist"
	sys.exit(1)

def remove_italic_bold(sentence):
	new_sentence = ""
	i = 0

	while i < len(sentence):
		if (sentence[i] == '<'):
			while True:
				i += 1
				if (sentence[i] == '>'):
					i += 1
					break;
		if (i < len(sentence)):
			new_sentence += sentence[i]
		i += 1
		
	return new_sentence

def replace_calls(sentence):
	sentence = sentence.replace('\n', ' ')
	sentence = sentence.replace('- ', '')
	sentence = sentence.replace('...', '')
	sentence = sentence.replace('...', '')
	sentence = sentence.replace('"', '')
	sentence = sentence.replace(':', '')
	return sentence

def convert_all_capital(sentence):
	for i in range(0, len(sentence)-1):
		if (sentence[i].isupper() & sentence[i+1].isupper()):
			return sentence.lower()
		else:
			return sentence

for i in range(0, len(subs)):
	subs[i] = subs[i].text #remove redunant information form srt parser
	subs[i] = remove_italic_bold(subs[i])
	subs[i] = replace_calls(subs[i])
	subs[i] = convert_all_capital(subs[i])










