'''
Link:
https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
'''
def DNA_strand(dna):
	cDNA = {
			'A':'T',
			'T':'A',
			'C':'G',
			'G':'C'
		}
	res = ''
	for char in dna:
		res += cDNA[char]
	return res

