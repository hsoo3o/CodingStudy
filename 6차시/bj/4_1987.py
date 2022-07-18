from collections import deque
import sys

def move(r,c):
    ans = 1
    q = set([(r,c,board[r][c])])
    while q:
        r,c,visit = q.pop()
        for d in [(-1,0),(1,0),(0,-1),(0,1)]:
            if r+d[0] < 0 or c+d[1] < 0 or r+d[0] >= R or c+d[1] >= C:
                continue
            if board[r+d[0]][c+d[1]] not in visit:
                q.add((r+d[0],c+d[1],visit+board[r+d[0]][c+d[1]]))
                ans = max(ans,len(visit + board[r+d[0]][c+d[1]]))
    print(ans)

R,C = map(int,sys.stdin.readline().split())
board = []

for _ in range(R):
    board.append(list(sys.stdin.readline().rstrip()))

move(0,0)
