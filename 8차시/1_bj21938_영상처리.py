import sys
sys.setrecursionlimit(10**5+1)

input = sys.stdin.readline
N,M = map(int,input().split())

RGB = []
mean_RGB = [[] for _ in range(N)]
for i in range(N):
    RGB.append(list(map(int, input().split())))
    
visited = [[0] * M for _ in range(N)]

th = int(input())

for i in range(N):
    for j in range(0,M*3,3):
        if sum(RGB[i][j:j+3])/3 < th:
            mean_RGB[i].append(0)
        else:
            mean_RGB[i].append(255)

dy = [1,-1,0,0]
dx = [0,0,1,-1]
        
def dfs(x,y):
    visited[y][x] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < M and 0 <= yy < N and visited[yy][xx] == 0 and mean_RGB[yy][xx] == 255:
            dfs(xx,yy)
    

cnt = 0
for y in range(M):
    for x in range(N):
        if visited[y][x] == 0 and mean_RGB[y][x] == 255:
            dfs(x,y)
            cnt += 1
print(cnt)