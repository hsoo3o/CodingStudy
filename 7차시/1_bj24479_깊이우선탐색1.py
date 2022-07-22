import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 1
def dfs(v):
    global cnt
    visited[v] = cnt
    for i in sorted(graph[v]):
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(R)

for ans in visited[1:]:
    print(ans)