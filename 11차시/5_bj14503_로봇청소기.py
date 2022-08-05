N,M = map(int,input().split())

# d = 0 : 북, 1 : 동, 2 : 남, 3 : 서
R,C,D = list(map(int,input().split())) # 1 1 0 : 1행1열 북쪽

graph = [list(map(int,input().split())) for _ in range(N)]
t_graph = [list(x) for x in zip(*graph)] 
print(t_graph)
# left = [0,-1]
cnt = 0
ch = [[0]*(M) for _ in range(N)]
print(ch)
def clean(r,c,d,spin,go):
    for _ in graph:
        print(_)

    global cnt
    print("r,c,d,spin,go:",r,c,d,spin,go)
    graph[r][c] = 1 # 청소했으면 2
    if ch[r][c]==0:
        cnt += 1
        ch[r][c] = 1
    if go == 1:
        return
    else:
        if d == 0:
            left = graph[r][:c]
            new_r = r
            new_c = c-1
            n_d = 3
            back_r = r+1
            back_c = c
        elif d == 1:
            left = t_graph[c][:r]
            new_r = r-1
            new_c = c
            n_d = 0
            back_r = r
            back_c = c - 1
        elif d == 2:
            left = graph[r][c+1:]
            new_r = r
            new_c = c + 1
            n_d = 1
            back_r = r-1
            back_c = c
        elif d == 3:
            left = t_graph[c][r+1:]
            new_r = r + 1
            new_c = c
            n_d = 2
            back_r = r
            back_c = c+1
        print(new_r,new_c,graph[new_r][new_c])
        print(back_r,back_c,graph[back_r][back_c])
        if 0 in left and graph[new_r][new_c] == 0:
            spin = 0
            clean(new_r,new_c,n_d,spin,0)
        elif 0 not in left or graph[new_r][new_c] == 1:
            # if graph[back_r][back_c] != 0:
            if spin != 4:
                spin += 1
                clean(r,c,n_d,spin,0)
            elif spin == 4:
                spin = 0
                if graph[back_r][back_c] == 1:
                    return
                if d == 0:
                    clean(r+1,c,d,spin,0)
                elif d == 1:
                    clean(r,c-1,d,spin,0)
                elif d == 2:
                    clean(r-1,c,d,spin,0)
                elif d == 3:
                    clean(r,c+1,d,spin,0)
            # else:
            
                

        

clean(R,C,D,0,0)

print(cnt)
