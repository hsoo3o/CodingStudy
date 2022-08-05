def dfs(l,sum_):
    global max_sum
    if l == n:
        if sum_ > max_sum:
            max_sum = sum_
    else:
        if l+tt[l] <= n:
            dfs(l+tt[l],sum_ + pp[l])
        dfs(l+1,sum_)


n = int(input())
tt = []
pp = []
max_sum = 0
for i in range(n):
    t,p = map(int,input().split())
    tt.append(t)
    pp.append(p)

dfs(0,0)
print(max_sum)