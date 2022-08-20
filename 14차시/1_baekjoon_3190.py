# Baekjoon 14891

from sys import stdin
from collections import deque

direction = list([[0,1], [1,0], [0,-1], [-1,0]])
direction_index = 0
snake_pos = deque([[0,0]])

N = int(stdin.readline())
K = int(stdin.readline())
apple_map = [[False for _ in range(N)] for _ in range(N)]
snake_map = [[False for _ in range(N)] for _ in range(N)]
t = 0

for i in range(K):
  row, col = list(map(int, stdin.readline().rstrip().split(' ')))
  apple_map[row-1][col-1] = True

schedule = deque()
L = int(stdin.readline())
for i in range(L):
  time, dir_ = list(stdin.readline().rstrip().split(' '))
  schedule.append([int(time), dir_])
while True:
  t += 1
  snake_head = snake_pos[-1]
  ny = snake_head[0]+direction[direction_index][0]
  nx = snake_head[1]+direction[direction_index][1]

  if 0 <= ny < N and 0 <= nx < N:
    if snake_map[ny][nx]:
      break
    snake_pos.append([ny, nx])
    snake_map[ny][nx] = True
    if apple_map[ny][nx]:
      apple_map[ny][nx] = False
    else:
      ry, rx = snake_pos.popleft()
      snake_map[ry][rx] = False
  else:
    break

  if schedule:
    if t == schedule[0][0]:
      if schedule[0][1] == "D":
        direction_index = (direction_index + 1) % 4
      else:
        direction_index = (direction_index - 1) % 4
      schedule.popleft()

print(t)