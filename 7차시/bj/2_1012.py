
import sys

def find(r,c):
    if soil[r][c] == 1:
        visited[r][c] = 1
        for i in range(4):
            rr = r + dx[i]
            cc = c + dy[i]
            if 0 <= rr < N and 0<= cc < M:
                if visited[rr][cc] == 0 and soil[rr][cc]:
                    visited[rr][cc] = 1
                    find(rr,cc)


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    cnt = 0
    M,N,K = map(int,sys.stdin.readline().split())

    soil = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        m,n = map(int,sys.stdin.readline().split())
        soil[n][m] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(N):
        for j in range(M):
            if soil[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                find(i,j)
                cnt += 1
    print(cnt)
    