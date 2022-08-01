# Baekjoon 16234

from sys import stdin
from collections import deque

N, L, R = list(map(int, stdin.readline().split()))

ans = 0
population = []
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(N):
    row = list(map(int, stdin.readline().split()))
    population.append(row)

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    is_exist = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                # Start BFS
                acc_val = population[i][j]
                count = 1
                position_mem = []
                queue = deque()
                queue.append([i,j])
                while len(queue) > 0:
                    cur = queue.popleft()
                    position_mem.append([cur[0],cur[1]])
                    for k in range(4):
                        x = cur[1] + dx[k]
                        y = cur[0] + dy[k]
                        if 0 <= x < N and 0 <= y < N:
                            if not visited[y][x]:
                                if L <= abs(population[y][x] - population[cur[0]][cur[1]]) <= R:
                                    queue.append([y, x])
                                    visited[y][x] = True
                                    count += 1
                                    acc_val += population[y][x]
                if count > 1:
                    is_exist = True
                    new_population = acc_val // count
                    for p in position_mem:
                        population[p[0]][p[1]] = new_population


    if not is_exist:
        break
    else:
        ans += 1

print(ans)