# Baekjoon 20055

from sys import stdin
from collections import deque

ans = 0
N, K = list(map(int, stdin.readline().rstrip().split(' ')))
conv_ = list(map(int, stdin.readline().rstrip().split(' ')))
conv = deque(conv_)
robot = deque([0 for _ in range(N)])
index = 0
count = 0
while True:
  ans += 1
  # 1. 회전
  conv.rotate()
  robot.rotate()
  robot[-1] = 0   # 내리는 위치

  # 2. 이동
  for i in range(N-2, -1, -1):
    if robot[i] != 0 and robot[i+1] == 0:
      if conv[i+1] != 0:
        conv[i+1] -= 1
        if conv[i+1] == 0:
          count += 1
        if i != N-2:
          robot[i+1] = 1
        robot[i] = 0

  # 3. 올림
  if conv[0] != 0:
    robot[0] = 1
    conv[0] -= 1
    if conv[0] == 0:
      count += 1

  # 4. 내구도 검사
  if count >= K:
    print(ans)
    break