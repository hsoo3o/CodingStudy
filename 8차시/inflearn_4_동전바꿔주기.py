import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
cp = []
cn = []
for i in range(k):
    p,n = map(int,input().split())
    cp.append(p)
    cn.append(n)
    
cnt = 0
def dfs(L,total):
    global cnt
    if total > T:
        return
    if total == T:
        cnt += 1 
        return
    if L == k:
        return
    else:
        for j in range(cn[L]+1):
            dfs(L+1,total+cp[L]*j)
                
dfs(0,0)

print(cnt)