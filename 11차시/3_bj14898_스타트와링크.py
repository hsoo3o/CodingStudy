import itertools

N = int(input())
ability = [[i+1] + list(map(int,input().split())) for i in range(N)]
ability.insert(0,[i for i in range(N+1)])
players = list(range(1,N+1))
candidate = list(itertools.combinations(players,int(N//2)))
ans = 999
for i in range(len(candidate)//2):
    team1 = list(itertools.permutations(candidate[i],2))
    team2 = list(itertools.permutations(candidate[-1-i],2))
    score1 = 0
    score2 = 0
    for tp in team1:
        p1,p2 = tp
        score1 += ability[p2][p1]
    for tp in team2:
        p1,p2 = tp
        score2 += ability[p2][p1]
    tmp = abs(score1-score2)
    if tmp < ans:
        ans = tmp
print(ans)

