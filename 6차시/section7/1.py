def dfs(l,sum_, time):
    global max_score
    if time > m:
        return
    if l == n:
        if sum_ > max_score:
            max_score = sum_
    else:
        dfs(l+1,sum_+pv[l],time+pt[l])
        dfs(l+1,sum_,time)


n,m = map(int,input().split())
pv = []
pt = []
for i in range(n):
    p,t = map(int,input().split())
    pv.append(p)
    pt.append(t)
max_score = 0


ch = [0]*n
dfs(0,0, 0)
print(max_score)