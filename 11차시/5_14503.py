from collections import deque
import sys


n,C = map(int,sys.stdin.readline().split())
robot = []
r,c,d =  map(int,sys.stdin.readline().split())
for _ in range(n):
    robot.append(list(map(int,sys.stdin.readline().split())))

q = deque([(r,c)])
move = [(0,-1,3,1,0),(-1,0,0,0,-1),(0,1,1,-1,0),(1,0,2,0,1)]
ch = 0
ans = 1
robot[r][c] = -1
while q:
    x,y = q.popleft()
    xx = x + move[d][0]
    yy = y + move[d][1]
    if ch < 4:
        if 0<= xx < n and 0<= yy < C:
            if robot[xx][yy] == 0:
                d = move[d][2]
                robot[xx][yy] = -1
                ans += 1
                q.append((xx,yy))
                ch = 0
            else:
                ch += 1
                d = move[d][2]
                q.append((x,y))
    else:
        xx = x + move[d][3]
        yy = y + move[d][4]
        if 0<= xx < n and 0<= yy < C:
            if robot[xx][yy] == 1:
                break
            else:
                q.append((xx,yy))
        ch = 0
print(ans)