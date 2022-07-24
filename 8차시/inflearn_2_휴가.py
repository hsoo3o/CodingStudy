n = int(input())
T = []
P = []
for i in range(n):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
res = -9999999999

def dfs(L,sum,date):
    global res
    if date > n:
        return
    if L > n:
        return
    if L == n:
        if sum > res:
            res = sum
        return
    else:
        t = T[L]
        dfs(L+t, sum+P[L], date+t)
        dfs(L+1, sum, date)
    return

dfs(0,0,0)

print(res)