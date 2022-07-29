# 1. 빙산 녹이기
# 2. 분리된 빙산의 개수 >= 2 
from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N,M = map(int,input().split())

ice = [list(map(int,input().split())) for _ in range(N)]
done = [[0]*M for _ in range(N)]

def dfs(r,c):
    global dr,dc
    vis[r][c] = True
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<N and 0<=nc<M and not ch[nr][nc] and ice[nr][nc] != 0:
            ch[nr][nc] = True
            
            dfs(nr,nc)
            ch[nr][nc] = False

year = 0
while True:
    ch = [[False]*M for _ in range(N)]
    q = deque()
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    for r in range(1,N):
        for c in range(1,M):
            if ice[r][c] == 0:
                for i in range(4):
                    nr = r+dr[i]
                    nc = c+dc[i]
                    if 0<=nr<N and 0<=nc<M and ice[nr][nc] != 0:
                        ice[nr][nc] -= 1

    # cnt하기
    ch = [[False]*M for _ in range(N)]
    vis = [[False]*M for _ in range(N)]
    cnt = 0
    for r in range(1,N):
        for c in range(1,M):
            if ice[r][c] != 0 and not vis[r][c]:
                if cnt == 2:
                    print(year+1)
                    break
                vis[r][c] = True
                dfs(r,c)
                cnt += 1
                
    year += 1
    if cnt == 1:
        pass
    elif ice == done:
        print(0)
    

