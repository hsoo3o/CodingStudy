import sys
input = sys.stdin.readline

N,M = map(int,input().split())
pv = []
pt = []

for i in range(N):
    score,time = map(int,input().split())
    pv.append(score)
    pt.append(time)
res = -999999999

def dfs(L,sum,time):
    global res
    if time > M:
        return
    if L == N:
        if sum > res:
            res = sum
    else:
        
        dfs(L+1,sum+pv[L], time+pt[L]) # 문제를 푼다
        dfs(L+1,sum,time) # 문제를 안풀고 넘어간다
        
dfs(0,0,0)

print(res)