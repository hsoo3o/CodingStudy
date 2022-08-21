from collections import deque
import sys

N,M = map(int,sys.stdin.readline().split())
game = []
for x in range(N):
    g = list(sys.stdin.readline())
    for y in range(M):
        if g[y] == "B":
            B = (x,y)
        elif g[y] == "R":
            R = (x,y)
        elif g[y] == "O":
            O = (x,y)
    game.append(g)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque([(1,R,B)])
while q:
    l,R,B = q.popleft()
    if l > 10:
        print(-1)
        exit()
    for i in range(4):
        rx,ry = R
        bx,by = B
        flag = False
        over = False
        break_B,break_R = False,False
        while True:
            rrx = rx + dx[i]
            rry = ry + dy[i]
            if 0<= rrx <N and 0<=rry<M:
                if (rrx,rry) != (bx,by):
                    if game[rrx][rry] == "O":
                        rx,ry = -1,-1
                        flag = True
                        break_R = True
                    elif game[rrx][rry] == "#":
                        break_R = True
                    else:
                        rx = rrx
                        ry = rry
                else:
                    break_R = True
            else:
                break_R = True
            bbx = bx + dx[i]
            bby = by + dy[i]
            if 0<=bbx <N and 0<=bby<M :
                if (bbx,bby) != (rx,ry):
                    if game[bbx][bby] == "O":
                        over = True
                        break_B = True
                    elif game[bbx][bby] == "#":
                        break_B = True
                    else:
                        bx = bbx
                        by = bby
                else:
                    break_B = True

            else:
                break_B = True
            if break_R and break_B:
                break
        if flag and not over:
            print(l)
            exit()
        if over:
            pass
        else:
            q.append([l+1,(rx,ry),(bx,by)])


