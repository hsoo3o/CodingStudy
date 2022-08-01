# Baekjoon 16236

from sys import stdin
from collections import deque
from copy import deepcopy
import sys

sys.setrecursionlimit(10**6)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(stdin.readline())

underthesea = []
time = 0
size = 2
feed = 0
position = [-1,-1]

for i in range(N):
    line = list(map(int, stdin.readline().split()))
    underthesea.append(line)
    if position == [-1,-1]:
        for k in range(N):
            if line[k] == 9:
                position = [i,k]
                break


while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    distance = 0
    visited[position[0]][position[1]] = True

    # BFS
    queue = deque()
    queue.append([position, 0])
    min_distance = 1e6
    candidate = []
    while queue:
        cur = queue.popleft()
        if cur[1] == min_distance:
            break
        for i in range(4):
            nx = cur[0][1] + dx[i]
            ny = cur[0][0] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx]:
                    if underthesea[ny][nx] <= size:
                        visited[ny][nx] = True
                        queue.append([[ny,nx],cur[1]+1])
                        if underthesea[ny][nx] != 0 and underthesea[ny][nx] < size:
                            candidate.append([ny,nx,cur[1]+1])
                            min_distance = cur[1]+1

    if len(candidate) == 0:
        print(time)
        exit(0)
    candidate.sort()
    y = candidate[0][0]
    x = candidate[0][1]
    underthesea[y][x] = 9
    underthesea[position[0]][position[1]] = 0
    position[0] = y
    position[1] = x
    feed += 1
    if feed == size:
        size += 1
        feed = 0
    time += candidate[0][2]