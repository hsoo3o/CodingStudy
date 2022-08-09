# Baekjoon 21610

from sys import stdin
import sys

N, M = list(map(int, stdin.readline().split())) 
ans = 0
grid = []
direction = {}
direction[1] = [0,-1]
direction[2] = [-1,-1]
direction[3] = [-1,0]
direction[4] = [-1,1]
direction[5] = [0,1]
direction[6] = [1,1]
direction[7] = [1,0]
direction[8] = [1,-1]
dx = [-1,-1,1,1]
dy = [1,-1,1,-1]

cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for i in range(N):
    grid.append(list(map(int, stdin.readline().split())))
for i in range(M):
    next_cloud = []
    d, s = list(map(int, stdin.readline().split())) 
    for k in range(len(cloud)):
        cloud[k][0] += s * direction[d][0]
        cloud[k][1] += s * direction[d][1]
        cloud[k][0] %= N
        cloud[k][1] %= N

        grid[cloud[k][0]][cloud[k][1]] += 1
    
    for k in range(len(cloud)):
        pos = cloud[k]
        for kk in range(4):
            nx = pos[1] + dx[kk]
            ny = pos[0] + dy[kk]
            if 0 <= nx < N and 0 <= ny < N:
                if grid[ny][nx] > 0:
                    grid[pos[0]][pos[1]] += 1

    visited = [[False for _ in range(N)] for _ in range(N)]
    for k in range(len(cloud)):
        pos = cloud[k]
        visited[pos[0]][pos[1]] = True
    for ii in range(N):
        for jj in range(N):
            if grid[ii][jj] >= 2:
                if not visited[ii][jj]:
                    grid[ii][jj] -= 2
                    next_cloud.append([ii,jj])
    cloud = next_cloud

ans += sum([sum(grid[i]) for i in range(N)])
print(ans)