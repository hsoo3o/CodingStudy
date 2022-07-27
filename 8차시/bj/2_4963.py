

from collections import deque
import sys


while True:
    w,h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    maps = []
    for _ in range(h):
        maps.append(list(map(int, sys.stdin.readline().split())))

    ch = [[0 for _ in range(w)] for _ in range(h)]
    dx = [-1,1,0,0,1,-1,1,-1]
    dy = [0,0,-1,1,1,-1,-1,1]
    ans = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and ch[i][j] == 0:
                ch[i][j] = 1
                q = deque([(i,j)])
                while q:
                    x,y = q.popleft()

                    for k in range(8):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < h and 0 <= yy < w:
                            if ch[xx][yy] == 0 and maps[xx][yy] == 1:
                                ch[xx][yy] = 1
                                q.append((xx,yy))
                ans += 1

    print(ans)
