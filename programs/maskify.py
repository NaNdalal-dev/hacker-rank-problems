'''
Link:
https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
'''

def maskify(cc):
	l = len(cc)
	if l <= 4:
		return cc
	new_str = cc[l-4:]
	hash_str = ''
	for i in range(l-4):
		hash_str += '#'

	mask_str =  hash_str + new_str
	return mask_str
#print(maskify('4556364607935616'))