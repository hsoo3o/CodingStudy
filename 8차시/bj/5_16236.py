from collections import deque
import sys

def find(pos):
    q = deque([pos])
    eat = [[] for _ in range(N**2)]
    move = [[0]*N for _ in range(N)]
    ch = [[0]*N for _ in range(N)]
    while q:
        x,y = q.popleft()
        ch[x][y] = 1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx < N and 0<=yy <N and ch[xx][yy] == 0:
                if fishes[xx][yy] > baby:
                    pass
                elif move[xx][yy] == 0:
                    move[xx][yy] = move[x][y] + 1
                    if fishes[xx][yy] == baby or fishes[xx][yy] == 0:
                        q.append([xx,yy])
                    elif fishes[xx][yy] < baby:
                        eat[move[xx][yy]].append([xx,yy])
                        q.append([xx,yy])
    return eat


N = int(sys.stdin.readline())

fishes = []
baby = 2
for i in range(N):
    fish = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        if fish[j] == 9:
            start = (i,j)
            fish[j] = 0
    fishes.append(fish)

dx = [1,-1,0,0]
dy = [0,0,-1,1]
time = 0
ate = find(start)
cnt = 0
weight = 0
while cnt != len(ate):
    cnt = 0
    for i in range(len(ate)):
        if cnt+1 == len(ate):
            pos = -1
            break
        if len(ate[i]) == 0:
            cnt += 1
        elif len(ate[i]) == 1:
            x,y = ate[i][0]
            weight += 1
            if weight >= baby:
                baby += 1
                weight = 0
            time += i
            fishes[x][y] = 0
            pos = (x,y)
            break
        else:
            ate[i].sort()
            x,y = ate[i][0]
            weight += 1
            if weight >= baby:
                baby += 1
                weight = 0
            time += i
            fishes[x][y] = 0
            pos = (x,y)
            break
    if pos != -1:
        ate = find(pos)
    else:
        break

print(time)


