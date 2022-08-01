# Baekjoon 2573

from sys import stdin
from collections import deque
import sys


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = list(map(int, stdin.readline().split()))

ice = []
time = 0

for i in range(N):
    ice.append(list(map(int, stdin.readline().split())))


while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    count = 0
    # Separate check
    for i in range(1, N-1):
        for j in range(1, M-1):
            if not visited[i][j]:
                if ice[i][j] > 0:
                    count += 1
                    # BFS
                    queue = deque()
                    queue.append([i,j])
                    visited[i][j] = True
                    while queue:
                        cur = queue.popleft()
                        melt_down = 0
                        for k in range(4):
                            nx = cur[1] + dx[k]
                            ny = cur[0] + dy[k]
                            if not visited[ny][nx]:
                                if ice[ny][nx] == 0:
                                    melt_down += 1
                                else:
                                    queue.append([ny,nx])
                                    visited[ny][nx] = True
                        ice[cur[0]][cur[1]] = ice[cur[0]][cur[1]] - melt_down if ice[cur[0]][cur[1]] > melt_down else 0


    if count >= 2:
        print(time)
        break
    time += 1

    cleared = 0
    for i in range(N):
        cleared += sum(ice[i])

    if cleared == 0:
        print(0)
        break