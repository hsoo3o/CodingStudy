
from collections import deque
import sys

def find(i,j):
    global res,cnt
    res += 1
    q = deque()
    q.append([i,j])
    while q:
        x,y = q.popleft()
        num = ice[x][y]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0<= xx < N and 0<= yy < M and ch[xx][yy] == 0:
                if ice[xx][yy] != 0 :
                    cnt += 1
                    ch[xx][yy] = 1
                    q.append([xx,yy])
                elif ice[xx][yy] == 0 and num > 0:
                    num -= 1

        ice[x][y] = num

N,M = map(int, sys.stdin.readline().split())

ice = []
for _ in range(N):
    ice.append(list(map(int,sys.stdin.readline().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]


ans = 0

while True:
    break_ = False
    ch = [[0 for _ in range(M)] for _ in range(N)]
    res = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ch[i][j] == 0 and ice[i][j] != 0:
                cnt += 1
                ch[i][j] = 1
                find(i,j)  
    if res > 1:
        print(ans)
        break_ = True
        break
    if cnt == 0:
        print(0)
        break_ = True
        break
    
    ans += 1



