import sys
sys.setrecursionlimit(10**5)

def DFS(p,l,parent):
    global ans
    ch[p] = 1
    if p == p2:
        ans = l
        return
    if family[p]:
        for i in family[p]:
            if i == p2:
                ans = l+1
                return
            if not ch[i]:
                DFS(i,l+1,p)
    if ch[parent] != 1:
        p = parent
        for j in range(1,n+1):
            if parent in family[j]:
                parent = j
                break
        DFS(p, l+1, parent)


n = int(sys.stdin.readline())
ans = -1
p1,p2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
family = [[] for _ in range(n+1)]

parent = 0

ch = [0]*(n+1)
for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    if y == p1:
        parent = x

DFS(p1,0, parent)
print(ans)
