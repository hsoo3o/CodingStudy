from collections import deque
import sys

def find():
    global q
    while q:
        now_r,now_c = q.popleft()
        for i in range(4):
            rr = now_r + dx[i]
            cc = now_c + dy[i]
            if 0 <= rr < N and 0<= cc < M:
                if tomato[rr][cc] == 0:
                    tomato[rr][cc] = tomato[now_r][now_c] + 1
                    q.append((rr,cc))
        
M,N = map(int,sys.stdin.readline().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int,sys.stdin.readline().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()
no = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i,j))
find()

ans = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            sys.exit(0)
        else:
            ans = max(tomato[i][j],ans)
else:
    print(ans-1)
            