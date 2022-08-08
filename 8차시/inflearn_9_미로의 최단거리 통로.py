from collections import deque

table = []
for _ in range(7):
    table.append(list(map(int,input().split())))

dr = [1,-1,0,0]

dc = [0,0,1,-1]
ch = [[0] * 7 for _ in range(7)]

ans = 9999999999
possible = 0

dq = deque()
dq.append((0,0))
ch[0][0] = 1
while dq:
    now = dq.popleft()
    for i in range(4):
        nr = now[0] + dr[i]
        nc = now[1] + dc[i]
        if 0 <= nr < 7 and 0 <= nc < 7 and table[nr][nc] == 0:
            ch[nr][nc] = 1
            table[nr][nc] = table[now[0]][now[1]] + 1
            dq.append((nr,nc))
        
if table[6][6] == 0:
    print(-1)
else:
    print(table[6][6])

# import sys
# from collections import deque
# input = sys.stdin.readline
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# board = [list(map(int,input().split())) for _ in range(7)]
# dis  = [[0]*7 for _ in range(7)]
# Q  = deque()
# Q.append((0,0))
# board[0][0] = 1

# while Q:
#     tmp = Q.popleft()
#     for i in range(4):
#         x = tmp[0] + dx[i]
#         y = tmp[1] + dy[i]
#         if 0<=x<=6 and 0<=y<=6 and board[x][y] == 0:
#             board[x][y] = 1
#             dis[x][y] = dis[tmp[0]][tmp[1]] + 1
#             Q.append((x,y))
# if dis[6][6] == 0:
#     print(-1)
# else:
#     print(dis[6][6])