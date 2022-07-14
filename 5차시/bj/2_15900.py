from collections import deque
import sys

def find(v,l):
    global level, q
    ch[i] = 1
    for k in tree[v]:
        if not ch[k]:
            q.append((l,k))
            ch[k] = 1
            level[l].append(k)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
ch = [0]*(n+1)
level = [[] for _ in range(n)]
q = deque()
ans = 0

for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(1,n+1):
    if len(tree[i]) == 2:
        level[0].append(i)
        find(i,1)
        break
else:
    print("d")
    level[0].append(1)
    ans += 1
    find(1,2)
while q:
    t = q.popleft()
    if len(tree[t[1]]) == 1:
        ans +=t[0]
    find(t[1],t[0]+1)

if ans % 2 == 0:
    print("NO")
else:
    print("YES")
