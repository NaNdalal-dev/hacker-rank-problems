"""
Link:
https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python
"""

def warn_the_sheep(queue):
	if queue[-1] == "wolf":
		return "Pls go away and stop eating my sheep"
	i = 1

	for animal in queue[::-1]:
		if animal == "wolf":
			warining = f"Oi! Sheep number {i-1}! You are about to be eaten by a wolf!"
			return warining

		i += 1