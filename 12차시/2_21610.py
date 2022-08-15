import sys


N,M = map(int,sys.stdin.readline().split())
basket = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

direction = [0,(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
dx = [-1,1,-1,1]
dy = [1,-1,-1,1]

ch = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    d,mov = map(int,sys.stdin.readline().split())
    for c in range(len(cloud)):
        x,y = cloud[c]
        xx = x + direction[d][0]*mov
        yy = y + direction[d][1]*mov
        while xx >= N or yy >= N or xx < 0 or yy < 0:
            if xx >= N:
                xx = xx-N
            if yy >= N:
                yy = yy-N
            if xx < 0:
                xx = N+xx
            if yy < 0:
                yy = N+yy
        cloud[c] = (xx,yy)
        basket[xx][yy] += 1
        ch[xx][yy] = 1
    for c in range(len(cloud)):
        x,y = cloud[c]
        for i in range(4):
            xxx = x + dx[i]
            yyy = y + dy[i]
            if 0<= xxx < N and 0<= yyy <N and basket[xxx][yyy] > 0:
                basket[x][y] += 1
    cloud = []
    for i in range(N):
        for j in range(N):
            if ch[i][j] == 0 and basket[i][j] >=2:
                cloud.append((i,j))
                basket[i][j] -= 2
            else:
                ch[i][j] = 0
    
ans = 0
for i in basket:
    ans += sum(i)

print(ans)
