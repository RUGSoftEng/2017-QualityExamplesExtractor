from nltk.tokenize import sent_tokenize
import substract_srt

def get_sentences(sub):
	splitted_subs = sent_tokenize(sub)
	for sentence in splitted_subs:
		if (( len(sentence) <= 60) & (' ' in sentence) ): #no more then 60 chars, at least 2 words
			sentences.append(sentence)
	return sentences

subs = substract_srt.subs
sentences = []

for part in subs:
	sentences = get_sentences(part)
