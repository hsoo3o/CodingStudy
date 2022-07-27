

from collections import deque
import sys

def find(i,j,col, check, peo):
    q = deque([(i,j)])

    while q:
        x,y = q.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < N:
                if check[xx][yy] == 0 and peo[xx][yy] == col:
                    check[xx][yy] = 1
                    q.append((xx,yy))


N = int(sys.stdin.readline())

people = []
red = []

for _ in range(N):
    line = sys.stdin.readline().rstrip()
    people.append(list(line))
    redline = line.replace("G","R")
    red.append(list(redline))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ch = [[0 for _ in range(N)] for _ in range(N)]
redch = [[0 for _ in range(N)] for _ in range(N)]
ans = 0
redans = 0
for i in range(N):
    for j in range(N):
        color = people[i][j]
        redcolor = red[i][j]
        if ch[i][j] == 0:
            ch[i][j] = 1
            find(i,j,color,ch,people)
            ans += 1
        if redch[i][j] == 0:
            redch[i][j] = 1
            find(i,j,redcolor,redch,red)
            redans += 1

print(str(ans) + ' ' + str(redans))
        