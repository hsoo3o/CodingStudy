import sys
input = sys.stdin.readline
N,M = map(int,input().split())
numbers = [i for i in range(1,N+1)]
res = [0 for i in range(M)]
cnt = 0
def dfs(L):
    global cnt
    if L == M:
        for n in res:
            print(n,end=' ')
        cnt += 1
        print("")
        return
    else:
        
        for i in range(N):
            res[L] = i+1
            dfs(L+1)
dfs(0)
print(cnt)