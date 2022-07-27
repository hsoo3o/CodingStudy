import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


N = int(input())
RGB = []
for idx in range(N):
    RGB.append(list(input()))
visited = [[False] * N for _ in range(N)]
visited1 = [[False] * N for _ in range(N)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(c,r):
    global color
    visited[c][r] = True
    for i in range(4):
        nc = c + dy[i]
        nr = r + dx[i]
        if 0 <= nc < N and 0 <= nr < N:
            if not visited[nc][nr] and RGB[nc][nr] == color:
                dfs(nc,nr)

def dfs1(c,r):
    global color1
    if color1 == 0:
        visited1[c][r] = True
        for i in range(4):
            nc = c + dy[i]
            nr = r + dx[i]
            if 0 <= nc < N and 0 <= nr < N:
                if not visited1[nc][nr] and (RGB[nc][nr] == 'R' or RGB[nc][nr] == 'G'):
                    dfs1(nc,nr)
    elif color1 == 1:
        visited1[c][r] = True
        for i in range(4):
            nc = c + dy[i]
            nr = r + dx[i]
            if 0 <= nc < N and 0 <= nr < N:
                if not visited1[nc][nr] and RGB[nc][nr] == 'B':
                    dfs1(nc,nr)
cnt = 0
cnt1 = 0

for c in range(N):
    for r in range(N):
        if not visited[c][r]:
            color = RGB[c][r]
            dfs(c,r)
            cnt += 1
        if not visited1[c][r]:
            color = RGB[c][r]
            if color == 'R' or color == 'G':
                color1 = 0
            elif color == 'B':
                color1 = 1
            dfs1(c,r)
            cnt1 += 1
                         
print(cnt, cnt1)