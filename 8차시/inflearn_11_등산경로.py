N = int(input())

mt = [list(map(int,input().split())) for _ in range(N)]
bot = 999999
top = 0
bx = 0
by = 0

tx = 0
ty = 0
for i in range(N):
    for j in range(N):
        tmp = mt[i][j]
        if tmp < bot:
            bot = tmp
            bx = j
            by = i
        elif tmp > top:
            top = tmp
            tx = j
            ty = i
cnt = 0
mt[0][0] = 1

dr = [1,-1,0,0]
dc = [0,0,1,-1]
ch = [[0]*N for _ in range(N)]
ch[0][0] = 1
def dfs(r,c):
    global cnt
    if r == ty and c == tx:
        cnt += 1
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<N and ch[nr][nc] == 0 and mt[r][c] < mt[nr][nc]:
                ch[nr][nc] = 1
                dfs(nr,nc)
                ch[nr][nc] = 0
dfs(by,bx)

print(cnt)