import sys

def dfs(l,ans,row,col):
    global map_
    map_[row][col] = 1
    if l == n:
        if row != 0 or col != 0:
            res.append(ans)
    else:
        for i in range(4):
            if row+dx[i] > 2*n+1 and row+dx[i] < 0 and col+dy[i] > 2*n+1 and col+dy[i] < 0:
                continue
            if map_[row+dx[i]][col+dy[i]] == 1:
                continue
            if prob[i]:
                map_[row+dx[i]][col+dy[i]] = 1
                dfs(l+1,ans*prob[i]/100,row+dx[i],col+dy[i])
                map_[row+dx[i]][col+dy[i]] = 0

n,E,W,N,S = map(int,sys.stdin.readline().split())

map_ = [[0 for _ in range(2*n+1)] for _ in range(2*n+1)]
prob = [E,W,N,S]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 1
res = []
row,col = n,n

dfs(0,ans,row,col)
print(sum(res))
