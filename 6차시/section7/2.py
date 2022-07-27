
def dfs(l,money):
    global max_money
    if l == n:
        if money >= max_money:
            max_money = money
    else:
        if l + pt[l] <= n:
            dfs(l+pt[l], money + pp[l])
        dfs(l+1, money )


n = int(input())

pt= []
pp = []

for _ in range(n):
    t,p = map(int,input().split())
    pt.append(t)
    pp.append(p)

ch = [0]*n
max_money = 0
dfs(0,0)
print(max_money)