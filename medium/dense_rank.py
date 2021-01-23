'''
Climbing the Leaderboard:
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
'''
def climbingLeaderboard(scores, alice_score):
	alice_rank=[]
	scores=set(scores)
	for alice in alice_score:	
		scores.append(alice)
		scores=sorted(set(scores),reverse=True)
		alice_rank.append(scores.index(alice)+1)
	return alice_rank
	
