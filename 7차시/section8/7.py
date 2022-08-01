
n = int(input())
v = []

for _ in range(n):
    v.append(list(map(int, input().split())))

dy = [[0] * n for _ in range(n)]
dy[0][0] = v[0][0]

for i in range(n):
    for j in range(n):
        if i == 0:
            dy[i][j] = dy[i][j-1] + v[i][j]
        elif j == 0:
            dy[i][j] = dy[i-1][j] + v[i][j]
        else:
            dy[i][j] = min(dy[i-1][j],dy[i][j-1]) + v[i][j]

print(dy[-1][-1])