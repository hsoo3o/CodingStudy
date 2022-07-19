N,M = map(int,input().split())

relations = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    A,B = map(int,input().split())
    relations[A].append(B)

def dfs(L,cnt):
    cnt += 1
    visited[L]

dfs(1,cnt)
