# 말의 총 횟수 = 홀수일 때 승리
# sum(루트노드 ~ 리프노드) % 2 != 0 이면 성원 승리

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

cnt = 0

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(n):
    visited[n] = True
    for i in tree[n]:
        if not visited[i]:
            depth[i] = depth[n] + 1
            dfs(i)

dfs(1)

for i in range(2,N+1):
    if len(tree[i]) == 1:
        cnt += depth[i]

if (cnt % 2 == 0):
    print("No")
else:
    print("Yes")