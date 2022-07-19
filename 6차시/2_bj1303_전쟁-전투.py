# N,M = map(int,input().split())

# soldiers = [0 for _ in range(M)]
# visitied = [[0]*(N) for _ in range(M)]
# done = [[1]*(N) for _ in range(M)]

# for idx in range(M):
#     soldiers[idx] =list(input())

# def dfs(low,col):
#     # visitied[low,col] = 1
#     if visitied[low][col] == 1:
#         return
#     else:
#         if visitied[low][col] == 0 and soldiers[low][col] == 'W':
#             visited[low][col] = 1
n,m = map(int,input().split())
graph = []
w_location = []
b_location = []
for i in range(m):
    graph.append(list(map(str,input())))
    for j in range(n):
        if graph[i][j]=='W':
            w_location.append([i,j])
        else:
            b_location.append([i,j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
 
def dfs(x,y,color):
    global cnt
    cnt+=1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<m and 0<=yy<n and graph[xx][yy]==color and visited[xx][yy]==0: #만약 범위 내의 좌표이고, 방문하지 않았으면 dfs
            visited[xx][yy] = visited[x][y]+1
            dfs(xx,yy,color)
           
# W 체크
visited = [[0]*n for _ in range(m)]
cnt_w = 0
for x,y in w_location:
    cnt = 0
    if visited[x][y]==0: # 처음 방문했을 때, 방문수를 1로 늘려줌(병사의 수 count)
        visited[x][y] = 1
        dfs(x,y,'W')
    cnt_w += cnt**2
print(cnt_w,end=' ')
 
# B 체크
visited = [[0]*n for _ in range(m)]
cnt_b = 0
for x,y in b_location:
    cnt = 0
    if visited[x][y]==0:
        visited[x][y] = 1
        dfs(x,y,'B')
    cnt_b += cnt**2
print(cnt_b,end=' ')
