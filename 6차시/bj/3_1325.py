from collections import deque
import sys

def BFS(computer):
    global cnt
    ch = [0 for _ in range(n+1)]
    q = deque([computer])
    ch[computer] = 1
    while q:
        com = q.popleft()
        cnt += 1
        for i in computers[com]:
            if ch[i] == 0:
                ch[i] = 1
                q.append(i)



n,m = map(int,sys.stdin.readline().split())

computers = [[] for _ in range(n+1)]
max = -1
ans = []

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    computers[b].append(a)

for i in range(1,n+1):
    cnt = 0
    if len(computers[i]) != 0:
        BFS(i)
    if cnt > max:
        ans.clear()
        max = cnt
        ans.append(i)
    elif cnt == max:
        ans.append(i)
    

for i in ans:
    print(i ,end=' ')