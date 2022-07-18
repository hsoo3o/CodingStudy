
import sys
sys.setrecursionlimit(10**5)
def find(v,l):
    global ans
    ch[v] = 1
    if v !=1 and len(tree[v]) == 1:
        ans += l

    for k in tree[v]:
        if ch[k]==0:
            find(k,l+1)
    


n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
ch = [0]*(n+1)

ans = 0

for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


find(1,0)
if ans % 2 == 0:
    print("NO")
else:
    print("YES")
