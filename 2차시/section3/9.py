n = int(input())
m = [list(map(int,input().split(' '))) for _ in range(n)]
z = [0 ]* (n+1)
m.insert(0,z)
m.append(z)
cnt = 0
for i in range(1,n+1):
    for j in range(0,n):
        if j == 0:
            a,b,c,d = m[i-1][j],0,m[i+1][j],m[i][j+1]
        elif j == n-1:
            a,b,c,d = m[i-1][j],m[i][j-1],m[i+1][j],0
        else:
            a,b,c,d = m[i-1][j],m[i][j-1],m[i+1][j],m[i][j+1]

        if (m[i][j] > a) and (m[i][j] >b ) and (m[i][j] >c ) and (m[i][j] > d):
            cnt += 1
print(cnt)