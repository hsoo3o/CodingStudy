import sys
N = int(input())

classroom = [[0 for _ in range(N)] for _ in range(N)]
student = {i:[] for i in range(1,N+1) }

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(N**2):
    student_like = list(map(int,sys.stdin.readline().split()))
    student[student_like[0]] = student_like[1:]
    like =  [[0 for _ in range(N)] for _ in range(N)]
    empty_ = [[0 for _ in range(N)] for _ in range(N)]
    now = [0,0,0]
    now_ = []
    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 0:
                for k in range(4):
                    ii = dx[k] + i
                    jj = dy[k] + j
                    if 0<= ii < N and 0<= jj <N:
                        if classroom[ii][jj] in student_like[1:]:
                            like[i][j] += 1
                        elif classroom[ii][jj] == 0 :
                            empty_[i][j] += 1
                if like[i][j] >= 0:
                    if now[0] < like[i][j]:
                        now = like[i][j],i,j
                    elif now[0] == like[i][j]:
                        if empty_[now[1]][now[2]] < empty_[i][j]:
                            now = like[i][j],i,j
                        elif empty_[now[1]][now[2]] == empty_[i][j]:
                            now_.append([0,i,j])
                if now[0] == 0 and like[i][j] == 0 and empty_[i][j] == 0:
                    now_.append([0,i,j])

                
    if type(now) == list:
        classroom[now_[0][1]][now_[0][2]] = student_like[0]
    else:
        classroom[now[1]][now[2]] = student_like[0]
happy = [0,1,10,100,1000]
ans = 0
tmp = 0
for x in range(N):
    for y in range(N):
        for k in range(4):
            xx = dx[k] + x
            yy = dy[k] + y
            if 0<= xx < N and 0<= yy <N:
                for s in  student[classroom[x][y]]:
                    if classroom[xx][yy] == s:
                        tmp += 1
    
        ans += happy[tmp]
        tmp = 0
print(ans)




