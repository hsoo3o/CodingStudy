from collections import deque
import sys
sys.setrecursionlimit(10**5)
def find(x,y):
    openN.append((x,y))
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < N:
            if ch[xx][yy] == 0 and L <= abs(nation[x][y] - nation[xx][yy]) <= R:
                find(xx,yy)




N,L,R = map(int, sys.stdin.readline().split())

nation = []

for _ in range(N):
    nation.append(list(map(int, sys.stdin.readline().split())))

ans = 0


dx = [-1,1,0,0]
dy = [0,0,-1,1]
while True:
    break_ = True
    ch = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            openN = []
            union = 0
            if ch[i][j] != 1:
                find(i,j)

                if len(openN)> 1:
                    break_ = False
                
                    for x, y in openN:
                        union += nation[x][y]
                    change = union//len(openN)
                    
                    for x, y in openN:
                        nation[x][y] = change
                    

    if break_:
        break
    ans += 1

print(ans)