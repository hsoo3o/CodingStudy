# 1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
from collections import deque
N = int(input())
K = int(input())

apples = [list(map(int,input().split())) for _ in range(K)]

L = int(input())

directions = [list(input().split()) for _ in range(L)]

table = [list(0 for _ in range(N)) for _ in range(N)]

for (row,col) in apples:
    row -= 1
    col -= 1
    table[row][col] = 'a'

s = deque()
s.append((0,0))
time = 0
direction = [0,1]
table[0][0] = 's'


def change_dir(now_direction,change_direction): # [1,0] - 아래로, [-1,0] - 위로, [0,1] - 오른쪽으로, [0,-1] - 왼쪽으로
    if change_direction == 'D': # 오른쪽으로 90도 방향 회전
        if now_direction == [1,0]:
            new_direction = [0,-1]
        elif now_direction == [-1,0]:
            new_direction = [0,1]
        elif now_direction == [0,1]:
            new_direction = [1,0]
        elif now_direction == [0,-1]:
            new_direction = [-1,0]
    elif change_direction == 'L':
        if now_direction == [1,0]:
            new_direction = [0,1]
        elif now_direction == [-1,0]:
            new_direction = [0,-1]
        elif now_direction == [0,1]:
            new_direction = [-1,0]
        elif now_direction == [0,-1]:
            new_direction = [1,0]
    return new_direction
idx = 0    
while True:
    time += 1
    if idx < len(directions):
        if time == int(directions[idx][0])+1:
            direction = change_dir(direction,directions[idx][1])
            idx += 1
    first_row = s[0][0]
    first_col = s[0][1]

    # 종료 조건
    if not (0 <= first_row < N and 0 <= first_col < N):
        print(time)
        break


    # 1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.

    nr = first_row + direction[0]
    nc = first_col + direction[1]

    # 종료 조건
    if not (0 <= nr < N and 0 <= nc < N) or table[nr][nc] == 's':
        print(time)
        break
    
    # 2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if table[nr][nc] == 'a':
        table[nr][nc] = 's'
        s.appendleft((nr,nc))
    # 3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    else:
        table[nr][nc] = 's'
        s.appendleft((nr,nc))
        last_row,last_col = s.pop()
        table[last_row][last_col] = 0

