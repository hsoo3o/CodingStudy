import sys
sys.setrecursionlimit(10**5)
N,M = map(int,input().split())

# d = 0 : 북, 1 : 동, 2 : 남, 3 : 서
R,C,D = list(map(int,input().split())) # 1 1 0 : 1행1열 북쪽

graph = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
ch = [[0]*(M) for _ in range(N)]
# print(ch)

def new_pos(d,r,c):
    if d == 0:
        left = graph[r][c-1]
        new_r = r
        new_c = c-1
        n_d = 3
        back_r = r+1
        back_c = c
    elif d == 1:
        left = graph[r-1][c]
        new_r = r-1
        new_c = c
        n_d = 0
        back_r = r
        back_c = c - 1
    elif d == 2:
        left = graph[r][c+1]
        new_r = r
        new_c = c + 1
        n_d = 1
        back_r = r-1
        back_c = c
    elif d == 3:
        left = graph[r+1][c]
        new_r = r + 1
        new_c = c
        n_d = 2
        back_r = r
        back_c = c+1
    return left,new_r,new_c,n_d,back_r,back_c

def clean(r,c,d,spin):
    print("")
    for _ in ch:
        print(_)
    global cnt
    # graph[r][c] = 1
    if ch[r][c]==0:
        cnt += 1
        ch[r][c] = 1
    left,new_r,new_c,n_d,back_r,back_c = new_pos(d,r,c)
    print("r,c,d,spin,left,new_r,new_c,n_d,back_r,back_c \n",r,c,d,spin,left,new_r,new_c,n_d,back_r,back_c)
    if spin != 4:
        if left == 0 and ch[new_r][new_c] == 0:
            clean(new_r,new_c,n_d,0)
        elif left == 1 or ch[new_r][new_c] == 1:
            clean(r,c,n_d,spin+1)
    elif spin == 4: # spin == 4
        if graph[back_r][back_c] == 1:
            return
        else:
            clean(back_r,back_c,d,0)   
            
clean(R,C,D,0)

print(cnt)
