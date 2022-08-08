from collections import deque
table=[list(map(int,input().split())) for _ in range(7)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

cnt = 0

ch = [[0]*7 for _ in range(7)]
ch[0][0] = 1
def dfs(r,c,ch):
    global dr,dc,cnt
    if r == 6 and c == 6:
        cnt += 1
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<7 and 0<=nc<7 and ch[nr][nc] == 0 and table[nr][nc] == 0:
                ch[nr][nc] = 1
                dfs(nr,nc,ch)
                ch[nr][nc] = 0

dfs(0,0,ch)

print(cnt)

# 최단거리 -> BFS, 가지의 수 -> DFS
# DFS 돌때는 DFS 끝나고 ch 원래대로 되돌려주는 것 잊지 말기
# BFS에서 격자판 탐색은 한 점을 중심으로 동심원으로 퍼져나가는 것
# DFS는 한 방향으로 쭉 뻗어나가는 것