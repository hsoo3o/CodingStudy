
import sys
sys.setrecursionlimit(10**5)
def dfs(R):
    global cnt
    cnt += 1
    visited[R] = 1  
    ans[R] = cnt
    for x in graph[R]:
        if visited[x] == 0:
            visited[x] = 1
            dfs(x)


n,m,r = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
cnt = 0
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

dfs(r)

for i in range(1,n+1):
    print(ans[i])