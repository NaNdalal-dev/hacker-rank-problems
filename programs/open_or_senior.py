'''
Link:
https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
'''
def open_or_senior(data):
    results = []

    for val in data:
    	age,handicap = val
    	if age >= 55 and handicap > 7:
    		results.append('Senior')
    	else:
    		results.append('Open')
    return results