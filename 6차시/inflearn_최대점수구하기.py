N,M = map(int,input().split())
score = [0 for _ in range(N+1)]
times = [0 for _ in range(N+1)]


for i in range(1,N+1):
    q,c = map(int,input().split())
    score[i] = q
    times[i] = c

ans = -99999999
time=0
tmp = 0
def dfs(L):
    global tmp,ans,time,times
    if time > M:
        tmp -= score[L-1]
        time -= times[L-1]
        return
    if L > N:
        if tmp > ans:
            ans = tmp
        tmp -= score[L-1]
        time -= times[L-1]
        return
    else:
        tmp += score[L]
        time += times[L]
        dfs(L+1)
        dfs(L+1)
dfs(1)
print(ans)

# def DFS(L,sum,time):
#     if L == N:
#         if sum > res:
#             res = sum
#     else:
#         DFS(L+1, sum+pv[L], time+pt[L])
#         DFS(L+1, sum,)