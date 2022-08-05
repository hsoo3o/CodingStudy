import sys


n,m = map(int,sys.stdin.readline().split())
candy = []
dy = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    candy.append(list(map(int,sys.stdin.readline().split())))

dy[0][0] = candy[0][0]
for i in range(1,m):
    dy[0][i]=dy[0][i-1]+candy[0][i]
for i in range(1,n):
    dy[i][0]=dy[i-1][0]+candy[i][0]

for i in range(1,n):
    for j in range(1,m):
        dy[i][j] = max(dy[i-1][j],dy[i][j-1],dy[i-1][j-1]) + candy[i][j]
print(dy[n-1][m-1])