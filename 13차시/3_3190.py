from collections import deque
import sys

apple = []
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
for _ in range(K):
    apple.append(list(map(int,sys.stdin.readline().split())))

dir = deque()
L = int(sys.stdin.readline())
for _ in range(L):
    t,direction = sys.stdin.readline().split()
    dir.append((int(t),direction))


board = [[0 for _ in range(N)] for _ in range(N)]
snake = [(0,0)]
r,c = 0,0
board[r][c] = 1
time = 0
head_dir = 0
#R,L,U,D
head_dir_change = [{"G":(0,1,0),"L":(-1,0,2),"D":(1,0,3)},
                    {"G":(0,-1,1),"L":(1,0,3),"D":(-1,0,2)},
                    {"G":(-1,0,2),"L":(0,-1,1),"D":(0,1,0)},
                    {"G":(1,0,3),"L":(0,1,0),"D":(0,-1,1)},]
while True:
    if dir and time == dir[0][0]:
        change = head_dir_change[head_dir]
        dr,dc,head_dir = change[dir[0][1]]
        dir.popleft()
    else:
        change = head_dir_change[head_dir]
        dr,dc,head_dir = change["G"]
    rr = r + dr
    cc = c + dc
    if 0 <= rr < N and 0<= cc <N and board[rr][cc] == 0:
        board[rr][cc] = 1
        snake.insert(0,(rr,cc))
        time += 1
        for i in range(len(apple)):
            if [rr+1,cc+1] == apple[i]:
                if i+1 < K:
                    apple = apple[0:i] + apple[i+1:]
                else:
                    apple.pop()
                break
        else:
            tail_r,tail_c = snake.pop()
            board[tail_r][tail_c] = 0

        r = rr
        c = cc
    else:
        break


print(time+1)
    