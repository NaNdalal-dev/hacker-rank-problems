'''
Halloween Sale:
https://www.hackerrank.com/challenges/halloween-sale/problem
'''
def howManyGames(p, d, m, s):
    if(s<p):
        return 0
    buy=1
    tot=p
    while s>=tot:            
        p-=d
        if(p<=m):
            tot+=m
            if tot>s:
                return buy
            else:
                buy+=1
        else:
            tot+=p
            if tot>s:
                return buy
            else:
                buy+=1
    return buy
