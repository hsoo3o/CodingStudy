import sys


N,M,x,y,K = map(int,sys.stdin.readline().split())
map_ = []

for _ in range(N):
    map_.append(list(map(int,sys.stdin.readline().split())))

order = list(map(int,sys.stdin.readline().split()))
dice = [0 for _ in range(6)]

for o in order:
    flag = False
    if o == 1:
        xx = x
        yy = y+1
        if 0 <= xx < N and 0 <= yy <M:
            flag = True
            dice = [dice[0],dice[4],dice[2],dice[5],dice[3],dice[1]]
            if map_[xx][yy] == 0:
                map_[xx][yy] = dice[3]
            else:
                map_[xx][yy], dice[3] = 0, map_[xx][yy]
            x = xx
            y = yy
    elif o == 2:
        xx = x
        yy = y-1
        if 0 <= xx < N and 0 <= yy <M:
            flag = True
            dice = [dice[0],dice[5],dice[2],dice[4],dice[1],dice[3]]
            if map_[xx][yy] == 0:
                map_[xx][yy] = dice[3]
            else:
                map_[xx][yy], dice[3] = 0, map_[xx][yy]
            x = xx
            y = yy
    elif o == 3:
        xx = x-1
        yy = y
        if 0 <= xx < N and 0 <= yy <M:
            flag = True
            dice = [dice[1],dice[2],dice[3],dice[0],dice[4],dice[5]]
            if map_[xx][yy] == 0:
                map_[xx][yy] = dice[3]
            else:
                map_[xx][yy], dice[3] = 0, map_[xx][yy]
            x = xx
            y = yy
    elif o == 4:
        xx = x+1
        yy = y
        if 0 <= xx < N and 0 <= yy <M:
            flag = True
            dice = [dice[3],dice[0],dice[1],dice[2],dice[4],dice[5]]
            if map_[xx][yy] == 0:
                map_[xx][yy] = dice[3]
            else:
                map_[xx][yy], dice[3] = 0, map_[xx][yy]
            x = xx
            y = yy
    if flag:
        print(dice[1])