
import sys

def find(r,c):
    global cnt
    cnt += 1
    if map[r][c] == '1':    
        visited[r][c] = 1
        for i in range(4):
            rr = r + dx[i]
            cc = c + dy[i]
            if 0 <= rr < N and 0<= cc < N:
                if visited[rr][cc] == 0 and map[rr][cc] == '1':
                    visited[rr][cc] = 1
                    find(rr,cc)

                    
map = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
N = int(sys.stdin.readline().rstrip())
visited = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    map.append(list(sys.stdin.readline().rstrip()))
sum_ = 0
ans = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if map[i][j] == '1' and visited[i][j] == 0:
            visited[i][j] = 1
            find(i,j)
            sum_ += 1
            ans.append(cnt)

print(sum_)
for i in sorted(ans):
    print(i)


