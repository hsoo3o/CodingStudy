
from collections import deque
import sys


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
    for i in range(N):
        for j in range(M):
            q = deque()
            cnt = 0
            if ch[i][j] == 0 and ice[i][j] != 0:
                ch[i][j] = 1
                cnt += 1
                res += 1
                q.append([i,j])
                while q:
                    x,y = q.popleft()
                    num = ice[x][y]
                    for i in range(4):
                        xx = x + dx[i]
                        yy = y + dy[i]

                        if 0<= xx < N and 0<= yy < M and ch[xx][yy] == 0:
                            if ice[xx][yy] != 0 :
                                ch[xx][yy] = 1
                                q.append([xx,yy])
                                cnt += 1
                            elif ice[xx][yy] == 0 and num > 0:
                                num -= 1
                                if num == 0:
                                    cnt -= 1
                            
                    ice[x][y] = num
        print(res, ice)
        if res > 1:
            print(ans)
            break_ = True
            break
        if cnt > 1:
            print(0)
            break_ = True
            break
    
    ans += 1
    if break_:
        break
            
