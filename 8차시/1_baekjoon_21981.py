# Baekjoon 21938

from sys import stdin
import sys
sys.setrecursionlimit(1000000) 
N, M = list(map(int, stdin.readline().split()))

ans = 0
image = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(N):
    row = list(map(int, stdin.readline().split()))
    for j in range(M):
        RGB = row[j*3:(j+1)*3]
        image[i][j] = RGB
threshold = int(stdin.readline())

def dfs(i,j):
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x < M and 0 <= y < N:
            if not visited[y][x]:
                if image[y][x] >= threshold:
                    visited[y][x] = True
                    dfs(y, x)


for i in range(N):
    for j in range(M):
        RGB = image[i][j]
        if sum(RGB) / 3 >= threshold:
            image[i][j] = 255
        else:
            image[i][j] = 0

for i in range(N):
    for j in range(M):
        if image[i][j] >= threshold and not visited[i][j]:
            visited[i][j] = True
            dfs(i,j)
            ans += 1

print(ans)