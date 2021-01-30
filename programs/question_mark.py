def QuestionsMarks(String):
	count = 0
	x = 0
	flag = 0
	for char in String:
		if char.isdigit():
			x += int(char)
			flag = 1

		if char == '?' and flag:
			count += 1
		if count == 3 and x == 10:
			return True

	return False
print(QuestionsMarks("acc?7??sss?3rr1??????5"))