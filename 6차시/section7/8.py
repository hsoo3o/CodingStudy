
from collections import deque


dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

ch = [[0]*n for _ in range(n)]
sum = 0
q = deque()
ch[n//2][n//2] = 1
sum += a[n//2][n//2]
q.append((n//2,n//2))
l = 0

while True:
    if l == n//2:
        print(sum)
        break
    else:
        for _ in range(len(q)):

            x,y = q.popleft()
            for i in range(4): 
                xx = x + dx[i]
                yy = y + dy[i]
                if ch[xx][yy] == 0:
                    ch[xx][yy] = 1
                    sum += a[xx][yy]
                    q.append((xx,yy))
        l += 1