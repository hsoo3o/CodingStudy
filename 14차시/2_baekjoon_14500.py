# Baekjoon 14500

from sys import stdin
from collections import deque

N, M = list(map(int, stdin.readline().rstrip().split(' ')))
paper = []
best_score = 0
for i in range(N):
  line = list(map(int, stdin.readline().rstrip().split(' ')))
  paper.append(line)

tetris = [
  [[0,0], [0,1], [0,2], [0,3]],
  [[0,0], [1,0], [2,0], [3,0]],
  [[0,0], [1,0], [1,1], [1,2]],
  [[0,0], [0,1], [1,0], [2,0]],
  [[0,0], [0,1], [0,2], [1,2]],
  [[0,0], [0,1], [-1,1], [-2,1]],
  [[0,0], [0,1], [0,2], [-1,2]],
  [[0,0], [1,0], [2,0], [2,1]],
  [[0,0], [1,0], [0,1], [0,2]],
  [[0,0], [0,1], [1,1], [2,1]],
  [[0,0], [0,1], [1,0], [1,1]],
  [[0,0], [0,1], [0,2], [-1,1]],
  [[0,0], [1,0], [1,1], [2,0]],
  [[0,0], [0,1], [0,2], [1,1]],
  [[0,0], [1,-1], [1,0], [2,0]],
  [[0,0], [0,1], [-1,1], [-1,2]],
  [[0,0], [1,0], [1,1], [2,1]],
  [[0,0], [0,1], [1,1], [1,2]],
  [[0,0], [0,1], [1,0], [-1,1]]
]

for i in range(N):
  for j in range(M):
    for t in tetris:
      continue_flag = False
      pos = [[i,j], [i+t[1][0], j+t[1][1]], [i+t[2][0], j+t[2][1]], [i+t[3][0], j+t[3][1]]]
      for p in pos:
        if 0 <= p[0] < N and 0 <= p[1] < M:
          pass
        else:
          continue_flag = True
          break
      if continue_flag:
        continue
      else:
        score = paper[pos[0][0]][pos[0][1]] + paper[pos[1][0]][pos[1][1]] + paper[pos[2][0]][pos[2][1]] + paper[pos[3][0]][pos[3][1]]
        best_score = score if score > best_score else best_score

print(best_score)

        
