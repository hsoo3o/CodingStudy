# Baekjoon 24479

from sys import stdin
import sys

sys.setrecursionlimit(1000000) 

N, M, R = list(map(int, stdin.readline().split()))

graph = {}
ans = [0 for _  in range(N)]
visited = [False for _  in range(N)]
count = 1
for i in range(N):
    graph[i+1] = []
for i in range(M):
    v1, v2 = list(map(int, stdin.readline().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(N):
    graph[i+1].sort(reverse=True)

def dfs(V):
    global count
    visited[V-1] = True
    ans[V-1] = count
    E = graph[V]
    while len(E) > 0:
        next_V = E.pop()
        if not visited[next_V-1]:
            count += 1
            dfs(next_V)

dfs(R)
for i in range(N):
    print(ans[i])