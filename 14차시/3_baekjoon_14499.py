# Baekjoon 14499

from sys import stdin
from collections import deque

dice = [0, 0, 0, 0, 0, 0] # 1, 2, 3, 4, 5, 6

N, M, x, y, K = list(map(int, stdin.readline().rstrip().split(' ')))
dice_map = []
for i in range(N):
  line = list(map(int, stdin.readline().rstrip().split(' ')))
  dice_map.append(line)
command = list(map(int, stdin.readline().rstrip().split(' ')))

dice_index = 0
pos = [x,y]

for c in command:
  if c == 1:
    ny, nx = pos[0], pos[1]+1
    if 0 <= ny < N and 0 <= nx < M:
      n_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    else:
      continue
  if c == 2:
    ny, nx = pos[0], pos[1]-1
    if 0 <= ny < N and 0 <= nx < M:
      n_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    else:
      continue
  if c == 3:
    ny, nx = pos[0]-1, pos[1]
    if 0 <= ny < N and 0 <= nx < M:
      n_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    else:
      continue
  if c == 4:
    ny, nx = pos[0]+1, pos[1]
    if 0 <= ny < N and 0 <= nx < M:
      n_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    else:
      continue
  
  dice = n_dice

  if dice_map[ny][nx] == 0:
    dice_map[ny][nx] = dice[5]
  else:
    dice[5] = dice_map[ny][nx]
    dice_map[ny][nx] = 0
  print(dice[0])
  pos = [ny,nx]
