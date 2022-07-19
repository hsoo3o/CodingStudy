N,pE,pW,pS,pN = map(int,input().split())


pEWSN = [pE,pW,pS,pN]
visited = [[0] * (2*N+1) for _ in range(2*N+1)]
visited[N][N] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans = 0

def dfs(x,y,cnt,p):
    global ans
    if cnt == N:
        ans += p
        return

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if visited[xx][yy]:
            continue
        if not 0 <= xx < (2*N) + 1 or not 0 <= yy < (2*N) + 1:
            continue
        visited[xx][yy] = 1
        dfs(xx,yy,cnt+1,p*pEWSN[i]/100)
        visited[xx][yy] = 0
dfs(N,N,0,1)
print(ans)