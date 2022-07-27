# N : 정점, M : 간선
# M개의 줄에 간선의 양 끝점 u,v
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N,M = map(int,input().split())

tree = [[]for _ in range(N+1)]

def dfs(s,d):
    visited[s] = True
    for i in tree[s]:
        if not visited[i]:
            dfs(i,d+1)
for i in range(M):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)
print("tree :", tree)
visited = [False] * (1+N)
cnt = 0

for i in range(1,N+1):
    if not visited[i]:
        if not tree[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i,0)
            cnt += 1

print(cnt)