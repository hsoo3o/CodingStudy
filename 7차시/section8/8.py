
def dfs(i,j):
    if dy[i][j] > 0:
        return dy[i][j] 
    if i == 0 and j == 0:
        return v[0][0]
    else:
        if j == 0:
            dy[i][j] = dfs(i-1,j) + v[i][j]
        elif i == 0:
            dy[i][j] = dfs(i,j-1) + v[i][j]
        else:
            dy[i][j] = min(dfs(i-1,j), dfs(i,j-1)) + v[i][j]
        return dy[i][j]


n = int(input())
v = []

for _ in range(n):
    v.append(list(map(int, input().split())))

dy = [[0] * n for _ in range(n)]
dy[0][0] = v[0][0]

print(dfs(n-1,n-1))