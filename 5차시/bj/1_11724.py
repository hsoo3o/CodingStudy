from collections import deque
import sys

def find(i):
    q = deque([i])
    ch[i] = 1
    while q:
        i = q.popleft()

        for k in v[i]:
            if not ch[k]:
                q.append(k)
                ch[k] = 1


n,m = map(int,sys.stdin.readline().split())
if m == 0 and n != 1:  #1 0 -> 1
    print(0)
else:
    v = [[] for _ in range(n+1)]
    for _ in range(m):
        v1,v2 = map(int,sys.stdin.readline().split())

        v[v2].append(v1)
        v[v1].append(v2)

    ch = [0]*(n+1)
    cnt = 0

    for i in range(1,n+1):
        if not ch[i]:
            find(i)
            cnt += 1
    print(cnt)

            



