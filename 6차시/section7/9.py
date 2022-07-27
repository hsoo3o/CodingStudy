
from collections import deque


board = [list(map(int, input().split())) for _ in range(7)]

dis = [[0]*7 for _ in range(7) ]

q = deque()
q.append((0,0))
board[0][0] = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
while q:
    x,y = q.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < 7 and 0 <= yy < 7 and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[x][y] +1
            q.append((xx,yy))

if dis[6][6] == 0:
    print(-1)
else: 
    print(dis[6][6])