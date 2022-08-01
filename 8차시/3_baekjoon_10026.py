# Baekjoon 10026

from sys import stdin
import sys
sys.setrecursionlimit(1000000) 
N = int(stdin.readline())

ans = 0
ans_RG = 0
image = []
visited = [[False for _ in range(N)] for _ in range(N)]
visited_RG = [[False for _ in range(N)] for _ in range(N)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(N):
    row = stdin.readline().rstrip()
    image.append(row)

def dfs(i,j, color):
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x < N and 0 <= y < N:
            if not visited[y][x]:
                if image[y][x] == color:
                    visited[y][x] = True
                    dfs(y, x, color)

def dfs_RG(i,j, color):
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x < N and 0 <= y < N:
            if not visited_RG[y][x]:
                if (color == 'B' and image[y][x] == color) or \
                   (color in ['R', 'G'] and image[y][x] in ['R', 'G']):
                    visited_RG[y][x] = True
                    dfs_RG(y, x, color)

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i,j, image[i][j])
            ans += 1

        if not visited_RG[i][j]:
            visited_RG[i][j] = True
            dfs_RG(i,j, image[i][j])
            ans_RG += 1
print(ans, ans_RG)