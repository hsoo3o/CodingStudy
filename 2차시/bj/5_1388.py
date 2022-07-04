n,m = map(int,input().split())
f = []
r = 0
c = 0
for _ in range(n):
    f.append(input())

for i in range(n):
    lastr = False
    for j in range(m):
        if f[i][j] == '-' and lastr:
            continue
        elif f[i][j] == '-':
            r += 1
            lastr = True
        elif f[i][j] == '|':
            lastr = False

        

for j in range(0,m):
    lastc = False
    for i in range(0,n):
        if f[i][j] == '-':
            lastc = False
        elif f[i][j] == '|' and lastc:
            lastr = False
            continue
        elif  f[i][j] == '|':
            lastr = False
            if i != n-1:
                lastc = f[i][j] == f[i+1][j]
            c += 1

print(r+c)
