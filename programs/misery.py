"""
Link:
https://www.codewars.com/kata/57ee31c5e77282c24d000024/train/python
"""

score_card = {
	"kata" : 5,
	"Petes kata" : 10,
	"life" : 0,
	"eating" : 1
}
def paul(x):
	total = 0
	for item in x:
		total += score_card[item]
	if total < 40:
		return 'Super happy!'

	elif total >= 40 and total < 70:
		return 'Happy!'

	elif total >= 70 and total < 100:
		return 'Sad!'
	return 'Miserable!'

print(paul(['Petes kata', 'Petes kata', 'eating', 'Petes kata', 'Petes kata', 'eating']))
print(paul(['life', 'Petes kata', 'Petes kata', 'Petes kata', 'eating']))
print(paul(['life', 'eating', 'life']))