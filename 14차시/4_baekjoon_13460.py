# Baekjoon 13460

from sys import stdin
from collections import deque


N, M = list(map(int, stdin.readline().rstrip().split(' ')))
board = []
empty_board = []
red_ball = []
blue_ball = []
for i in range(N):
  line = list(stdin.readline().rstrip())
  line_ = line.copy()
  for j in range(M):
    if line[j] == 'R':
      red_ball = [i,j]
      line_[j] = '.'
    if line[j] == 'B':
      blue_ball = [i,j]
      line_[j] = '.'
  board.append(line)
  empty_board.append(line_)

def board_manipulation(ball, motion):
  if motion == 1:
    for i in range(ball[1]-1, -1, -1):
      if empty_board[ball[0]][i] == 'O':
        return []
      elif empty_board[ball[0]][i] == '.':
        continue
      else:
        return [ball[0], i+1]

  elif motion == 2:
    for i in range(ball[1]+1, M, 1):
      if empty_board[ball[0]][i] == 'O':
        return []
      elif empty_board[ball[0]][i] == '.':
        continue
      else:
        return [ball[0], i-1]

  if motion == 3:
    for i in range(ball[0]-1, -1, -1):
      if empty_board[i][ball[1]] == 'O':
        return []
      elif empty_board[i][ball[1]] == '.':
        continue
      else:
        return [i+1, ball[1]]

  elif motion == 4:
    for i in range(ball[0]+1, N, 1):
      if empty_board[i][ball[1]] == 'O':
        return []
      elif empty_board[i][ball[1]] == '.':
        continue
      else:
        return [i-1, ball[1]]
  return ball

# motion: 1(왼쪽), 2(오른쪾), 3(위), 4(아래)
ball_pos = deque([[red_ball, blue_ball, 0, 0]])   # [red_ball, blue_ball, motion, count]

while ball_pos:
  current = ball_pos.popleft()
  red_ball = current[0]
  blue_ball = current[1]
  prev_motion = current[2]
  count = current[3]
  # print("---------------")
  # print(red_ball)
  # print(blue_ball)
  # print(prev_motion)
  # print(count)

  if len(red_ball) == 0:
    if len(blue_ball) == 0:
      continue
    print(count)
    exit(0)
  elif len(blue_ball) == 0:
    continue

  if count == 10:
    continue


  # print("*****************************")
  # for i in range(N):
  #   print(empty_board[i])
  # print("*****************************")

  # empty_board[red_ball[0]][red_ball[1]] = '.'
  # empty_board[blue_ball[0]][blue_ball[1]] = '.'

  # print("*****************************")
  # for i in range(N):
  #   print(empty_board[i])
  # print("*****************************")
  # print("*****************************")
  # print("*****************************")


  # 1
  if prev_motion != 1:
    next_pos = {}
    if red_ball[1] < blue_ball[1]:
      # red first
      next_pos['red_ball'] = board_manipulation(red_ball, 1)
      if len(next_pos['red_ball']) != 0:
        empty_board[next_pos['red_ball'][0]][next_pos['red_ball'][1]] = 'R'
      next_pos['blue_ball'] = board_manipulation(blue_ball, 1)
    else:
      next_pos['blue_ball'] = board_manipulation(blue_ball, 1)
      if len(next_pos['blue_ball']) != 0:
        empty_board[next_pos['blue_ball'][0]][next_pos['blue_ball'][1]] = 'B'
      next_pos['red_ball'] = board_manipulation(red_ball, 1)
    ball_pos.append([next_pos['red_ball'], next_pos['blue_ball'], 1, count+1])

    if len(next_pos['red_ball']) != 0:
      empty_board[next_pos['red_ball'][0]][next_pos['red_ball'][1]] = '.'
    if len(next_pos['blue_ball']) != 0:
      empty_board[next_pos['blue_ball'][0]][next_pos['blue_ball'][1]] = '.'
    empty_board[red_ball[0]][red_ball[1]] = '.'
    empty_board[blue_ball[0]][blue_ball[1]] = '.'
  # 2
  if prev_motion != 2:
    next_pos = {}
    if red_ball[1] < blue_ball[1]:
      # blue first
      next_pos['blue_ball'] = board_manipulation(blue_ball, 2)
      if len(next_pos['blue_ball']) != 0:
        empty_board[next_pos['blue_ball'][0]][next_pos['blue_ball'][1]] = 'B'
      next_pos['red_ball'] = board_manipulation(red_ball, 2)
    else:
      next_pos['red_ball'] = board_manipulation(red_ball, 2)
      if len(next_pos['red_ball']) != 0:
        empty_board[next_pos['red_ball'][0]][next_pos['red_ball'][1]] = 'R'
      next_pos['blue_ball'] = board_manipulation(blue_ball, 2)
    ball_pos.append([next_pos['red_ball'], next_pos['blue_ball'], 2, count+1])

    if len(next_pos['red_ball']) != 0:
      empty_board[next_pos['red_ball'][0]][next_pos['red_ball'][1]] = '.'
    if len(next_pos['blue_ball']) != 0:
      empty_board[next_pos['blue_ball'][0]][next_pos['blue_ball'][1]] = '.'
    empty_board[red_ball[0]][red_ball[1]] = '.'
    empty_board[blue_ball[0]][blue_ball[1]] = '.'
  # 3
  if prev_motion != 3:
    next_pos = {}
    if red_ball[0] < blue_ball[0]:
      # red first
      next_pos['red_ball'] = board_manipulation(red_ball, 3)
      if len(next_pos['red_ball']) != 0:
        empty_board[next_pos['red_ball'][0]][next_pos['red_ball'][1]] = 'R'
      next_pos['blue_ball'] = board_manipulation(blue_ball, 3)
    else:
      next_pos['blue_ball'] = board_manipulation(blue_ball, 3)
      if len(next_pos['blue_ball']) != 0:
        empty_board[next_pos['blue_ball'][0]][next_pos['blue_ball'][1]] = 'B'
      next_pos['red_ball'] = board_manipulation(red_ball, 3)
    ball_pos.append([next_pos['red_ball'], next_pos['blue_ball'], 3, count+1])

    if len(next_pos['red_ball']) != 0:
      empty_board[next_pos['red_ball'][0]][next_pos['red_ball'][1]] = '.'
    if len(next_pos['blue_ball']) != 0:
      empty_board[next_pos['blue_ball'][0]][next_pos['blue_ball'][1]] = '.'
    empty_board[red_ball[0]][red_ball[1]] = '.'
    empty_board[blue_ball[0]][blue_ball[1]] = '.'
  # 4
  if prev_motion != 4:
    next_pos = {}
    if red_ball[0] < blue_ball[0]:
      # blue first
      next_pos['blue_ball'] = board_manipulation(blue_ball, 4)
      if len(next_pos['blue_ball']) != 0:
        empty_board[next_pos['blue_ball'][0]][next_pos['blue_ball'][1]] = 'B'
      next_pos['red_ball'] = board_manipulation(red_ball, 4)
    else:
      next_pos['red_ball'] = board_manipulation(red_ball, 4)
      if len(next_pos['red_ball']) != 0:
        empty_board[next_pos['red_ball'][0]][next_pos['red_ball'][1]] = 'R'
      next_pos['blue_ball'] = board_manipulation(blue_ball, 4)
    ball_pos.append([next_pos['red_ball'], next_pos['blue_ball'], 4, count+1])

    if len(next_pos['red_ball']) != 0:
      empty_board[next_pos['red_ball'][0]][next_pos['red_ball'][1]] = '.'
    if len(next_pos['blue_ball']) != 0:
      empty_board[next_pos['blue_ball'][0]][next_pos['blue_ball'][1]] = '.'

print("-1")