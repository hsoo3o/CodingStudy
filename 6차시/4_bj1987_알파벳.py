R,C = map(int,input().split())

board = [0 for _ in range(R)]
visited = [[0]*(C+1) for _ in range(R+1)]

for i in range(R):
    board[i] = list(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,a):
    if visited[x][y] == 0:
        global cnt
        cnt += 1
        global alphabets
        alphabets.append(a)

        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]  

            if 0 <= xx < R and 0<= yy < C and visited[xx][yy] == 0:
                new_a = board[xx][yy]
                if new_a not in alphabets:
                    visited[xx][yy] = visited[x][y] + 1
                    print(board[xx][yy])
                    print("현재 x,y : ({},{}), 현재 i :{}, 더해진 dx,dy :({},{}), 다음 x,y : ({},{})".format(x,y,i,dx,dy))
                    dfs(xx,yy,board[xx][yy])
ans = -1
for _ in board:
    print(_)

for i in range(R):
    for j in range(C):
        visited = [[0]*(C+1) for _ in range(R+1)]
        print(i,j)
        print(board[i][j])
        alphabets = []
        # visited[i][j] = 1
        cnt = 0
        dfs(i,j,board[i][j])
        if cnt > ans:
            ans = cnt
        print("\n\n")
print(ans)