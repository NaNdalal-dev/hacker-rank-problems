'''
designer-pdf-viewer:
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
'''
def designerPdfViewer(h, word):
	l=len(word)
	alphabets=[chr(i) for i in range(97,123)]
	zipped=dict(zip(alphabets,h))
	letters=[]
	for letter in word:
		letters.append((zipped[letter]))
	
	maximum=letters[0]
	for i in range(1,len(letters)):
		if(maximum<letters[i]):
			maximum=letters[i]
	return maximum*l
