import sys
from collections import deque
sys.setrecursionlimit(10 ** 5) 


input = sys.stdin.readline

# BFS
# while True:
#     w,h = map(int,input().split()) # w : 열, h : 행
#     if (w,h) == (0,0):
#         break
#     ground = []
#     for i in range(h):
#         ground.append(list(map(int,input().split())))
#     ch = [[0]*w for _ in range(h)]
#     cnt = 0
#     for y in range(h):
#         for x in range(w):
#             if ground[y][x] == 1 and ch[y][x] == 0:
#                 ch[y][x] = 1
#                 dq = deque()
#                 dq.append([y,x])
#                 while dq:
#                     now = dq.popleft()
#                     y = now[0]
#                     x = now[1]
#                     dx = [1,-1,0,0,1,1,-1,-1]
#                     dy = [0,0,1,-1,1,-1,1,-1]
#                     for i in range(8):
#                         xx = x+dx[i]
#                         yy = y+dy[i]
#                         if 0 <= xx < w and 0 <= yy < h :
#                             if ch[yy][xx] == 0 and ground[yy][xx] == 1:
#                                 ch[yy][xx] = 1
#                                 dq.append([yy,xx])
#                 cnt += 1
#     print(cnt)

# DFS
def dfs(y,x):
    dx = [1,-1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    for i in range(8):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0 <= xx < w and 0 <= yy < h :
            if ch[yy][xx] == 0 and ground[yy][xx] == 1:
                ch[yy][xx] = 1
                dfs(yy,xx)
while True:
    w,h = map(int,input().split()) # w : 열, h : 행
    if (w,h) == (0,0):
        break
    ground = []
    for i in range(h):
        ground.append(list(map(int,input().split())))
    ch = [[0]*w for _ in range(h)]
    cnt = 0
    for y in range(h):
        for x in range(w):
            if ground[y][x] == 1 and ch[y][x] == 0:
                ch[y][x] = 1
                dfs(y,x)
                cnt += 1
    print(cnt)
    