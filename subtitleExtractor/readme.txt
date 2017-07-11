The python version used to make these codes is 2.7.6

The python nltk library should be installed (http://www.nltk.org/install.html)
The python pysrt package should be installed (https://pypi.python.org/pypi/pysrt)

Links sentences from subtitles to given words

Run: python main.py
Input 1: subtitle filename (do not include .srt, file should be in the same folder)
Input 2: words filename (do not include .txt, file should be in the same folder)

1. substract_srt: substracts sentences from a .srt file and removes irregularities
2. splitter_nltk: splits sentences with the nltk libabry and the restrictions: at least 2 words and no more then 60 characters
3. link: links the words from a .txt file with the sentences from the .srt file.
		 It sorts the words in alpabetical order. 
		 For every word in the sentences it does a binary search in the wordslist and places the matching sentences at the words.
4. main: lets 1-3 run and writes the output to a .txt file