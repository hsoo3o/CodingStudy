n = int(input())
g = [list(map(int,input().split(' '))) for _ in range(n)]

c = []
m = int(input())
for _ in range(m):
    r,d,num = list(map(int, input().split(' ')))
    num = num % n
    if d == 0:
        g[r-1]= g[r-1][num:] + g[r-1][:num]
    elif d == 1:
        g[r-1] = g[r-1][n-num:] + g[r-1][:n-num]
s=0
e = n
ans = 0
for i in range(n):
    ans += sum(g[i][s:e])
    print(g[i][s:e])
    if i < n//2:
        s += 1
        e -= 1
    else: 
        s -= 1
        e += 1
print(ans)



