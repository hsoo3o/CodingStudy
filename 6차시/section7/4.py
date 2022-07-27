
def dfs(l,sum_):
    global cnt
    if sum_ > T:
        return
    if l == k:
        if sum_ == T:
            cnt +=1
    else:
        for i in range(pn[l]+1):
            dfs(l+1, sum_ + pp[l]*i )


T = int(input())
k = int(input())

pp = []
pn = []
for _ in range(k):
    p,n = map(int,input().split())
    pp.append(p)
    pn.append(n)
cnt = 0

dfs(0,0)
print(cnt)