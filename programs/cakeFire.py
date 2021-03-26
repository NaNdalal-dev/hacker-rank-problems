'''
Link:
https://www.codewars.com/kata/5805ed25c2799821cb000005/train/python
'''

def cake(candles, debris):
	if candles == 0:
		return 'That was close!'
	candles70 = candles * 0.7
	result = 0
	index = 0
	for char in debris:
		if index%2 == 0:
			result += ord(char)
		else:
			result += ord(char) - 96
		index += 1
	if result > candles70:
		return "Fire!"
	return "That was close!"

print(cake(0,"jpipe"))