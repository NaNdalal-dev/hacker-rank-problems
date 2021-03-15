"""
Link:
https://www.codewars.com/kata/5b853229cfde412a470000d0/train/python
Your function takes two arguments:
	current father's age (years)
	current age of his son (years)
Сalculate how many years ago the father was twice as old as his son
(or in how many years he will be twice as old).
"""

twice_as_old = lambda dad_years_old, son_years_old: abs(dad_years_old - (son_years_old*2))

print(twice_as_old(55,30))
