# Baekjoon 4963

from sys import stdin
import sys
sys.setrecursionlimit(1000000) 

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    width, height = list(map(int, stdin.readline().split()))
    if width == 0 and height == 0:
        break
    land = []
    ans = 0
    visited = [[False for _ in range(width)] for _ in range(height)]
    for i in range(height):
        l = list(map(int, stdin.readline().split()))
        land.append(l)

    def dfs(row,col):
        for k in range(8):
            x = col + dx[k]
            y = row + dy[k]
            if 0 <= x < width and 0 <= y < height:
                if not visited[y][x]:
                    if land[y][x] == 1:
                        visited[y][x] = True
                        dfs(y,x)

    for r in range(height):
        for c in range(width):
            if not visited[r][c] and land[r][c] == 1:
                ans += 1
                dfs(r,c)

    print(ans)