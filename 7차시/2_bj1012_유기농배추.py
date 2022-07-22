import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

T = int(input())
for n in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*(M) for _ in range(N)]
    visited = [[0]*(M) for _ in range(N)]

    for i in range(K):
        X,Y = map(int,input().split())
        graph[Y][X] = 1
    
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]

    
    def dfs(x,y):
        global ox
        if visited[y][x] == 1 or graph[y][x] == 0:
            return
        elif visited[y][x] == 0 and graph[y][x] == 1:
            ox = 1
        visited[y][x] = 1
        for k in range(3):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx <= M-1 and 0 <= yy <= N-1 and visited[yy][xx] == 0:
                dfs(xx,yy)
    cnt = 0
    for i in range(M):
        for j in range(N):
            ox = 0
            dfs(i,j)
            if ox != 0:
                cnt += 1
    
    print("답:",cnt)