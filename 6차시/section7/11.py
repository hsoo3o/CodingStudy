
def dfs(x,y):
    global cnt
    if x == end[0] and y == end[1]:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N and ch[xx][yy] == 0 and moun[xx][yy] > moun[x][y]:
                ch[xx][yy] = 1
                dfs(xx,yy)
                ch[xx][yy] = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]
N = int(input())
moun = []
ch = [[0]*N for _ in range(N)]
start = (0,0)
end = (0,0)
mins = 2170000
maxe = -21700000
for i in range(N):
    mountain = list(map(int, input().split())) 
    for j in range(N):
        if mountain[j] < mins:
            mins = mountain[j]
            start = (i,j)
        if mountain[j] > maxe:
            maxe = mountain[j]
            end = (i,j)
    moun.append(mountain)

ch[start[0]][start[1]] = 1
cnt = 0
print(start,end)
dfs(start[0],start[1])
print(cnt)