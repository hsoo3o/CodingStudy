from collections import deque
import sys


N,M = map(int,sys.stdin.readline().split())

new_window = [[] for _ in range(N)]
ch = [[0 for _ in range(M)] for _ in range(N)]
window = []
for _ in range(N):
    window.append(list(map(int, sys.stdin.readline().split())))

T = int(sys.stdin.readline())

for i in range(len(window)):
    for j in range(0,len(window[i]),3):
        if sum(window[i][j:j+3])/3 >= T:
            new_window[i].append(255)
        else:
            new_window[i].append(0)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

for i in range(N):
    for j in range(M):
        if new_window[i][j] == 255 and ch[i][j] == 0:
            ch[i][j] == 1
            q = deque([(i,j)])
            while q:
                x,y = q.popleft()
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if 0 <= xx < N and 0 <= yy < M:
                        if ch[xx][yy] == 0 and new_window[xx][yy] == 255:
                            ch[xx][yy] = 1
                            q.append((xx,yy))
            ans += 1

print(ans)


