'''
Climbing the Leaderboard:
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
'''
def climbingLeaderboard(scores, alice_score):
	final_scores=set(scores+alice_score)
	print(final_scores)
	ranks=sorted(final_scores,reverse=True)
	print(ranks)
	res=[ranks.index(i)+1 for i in alice_score]
	print(res)
