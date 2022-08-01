from collections import deque
import sys

def dfs(x,y,sum_):
    global max_sum
    print(ch)
    if x == 1 and y == n-1:
        if sum_ > max_sum:
            max_sum = sum_
        return
    else:
        for i in range(x,2):
            for j in range(y,n):
                if ch[i][j] == 0:
                    if (i == x+1 and j == y) or (i == x-1 and j == y) or (i == x and j == y+1) or (i == x and j == y-1):
                        pass
                    else:
                        ch[i][j] = 1
                        dfs(i,j,sum_ + sticker[i][j])
                        ch[i][j] = 0




T = int(sys.stdin.readline())

for _ in range(T):
    sticker = []
    max_sum = 0
    res = []
    n = int(sys.stdin.readline())
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for _ in range(2):
        sticker.append(list(map(int, sys.stdin.readline().rstrip().split())))
    ch = [[0 for _ in range(n)] for _ in range(2)]
    dfs(0,0,sticker[0][0])
    dfs(1,0,sticker[1][0])
    dfs(0,0,sticker[0][0])
    print(max_sum)
    