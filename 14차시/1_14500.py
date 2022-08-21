import sys

def find(cnt,r,c,sum_,test):
    global max_sum
    if cnt == 3:
        if sum_ > max_sum:
            max_sum = sum_
        test = []
    else:
        for i in range(4):
            xx = r + dx[i]
            yy = c + dy[i]
            if 0<= xx <N and 0<= yy <M and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                find(cnt+1,xx,yy,sum_ + paper[xx][yy],test+[paper[xx][yy]])
                ch[xx][yy] = 0


N,M = map(int,sys.stdin.readline().split())
paper = []
ch = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
for _ in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))
    ch.append([0 for _ in range(M)])

max_sum = 0
ans = 0
for i in range(N):
    for j in range(M):
        ch[i][j] = 1
        find(0,i,j,paper[i][j],[paper[i][j]])
        if j-1 >= 0 and j+1 < M:
            if i-1 >= 0:
                sum_ = sum(paper[i][j-1:j+2])+paper[i-1][j]
                if sum_ > max_sum:
                    max_sum = sum_
            if i+1 < N:
                sum_ = sum(paper[i][j-1:j+2])+paper[i+1][j]
                if sum_ > max_sum:
                    max_sum = sum_
        if i-1 >= 0 and i+1 < N:
            if j-1 >= 0:
                sum_ = paper[i-1][j] + paper[i][j] + paper[i+1][j] + paper[i][j-1]
                if sum_ > max_sum:
                    max_sum = sum_
            if j+1 < M:
                sum_ = paper[i-1][j] + paper[i][j] + paper[i+1][j] + paper[i][j+1]
                if sum_ > max_sum:
                    max_sum = sum_
        if max_sum > ans:
            ans = max_sum
        ch[i][j] = 0

print(ans)

