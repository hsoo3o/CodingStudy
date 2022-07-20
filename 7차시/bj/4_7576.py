from collections import deque
import sys
sys.setrecursionlimit(10**5)
def find(v):
    global q, no
    if q:
        len_ = len(q)
        no += len_
        for i in range(len_):
            r,c = q.popleft()
            if tomato[r][c] == 1:
                for i in range(4):
                    rr = r + dx[i]
                    cc = c + dy[i]
                    if 0 <= rr < N and 0<= cc < M:
                        if tomato[rr][cc] == 0:
                            tomato[rr][cc] = 1
                            q.append((rr,cc))
        find(v+1)
    else:
        if no != N*M:
            print(-1)
        else:
            print(v-1)  



M,N = map(int,sys.stdin.readline().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0 for _ in range(M)] for _ in range(N)]
q = deque()
no = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i,j))
        elif  tomato[i][j] == -1:
            no += 1
find(0)
            