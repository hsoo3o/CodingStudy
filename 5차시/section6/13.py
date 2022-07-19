
def dfs(v):
    global cnt
    if v == n:
        cnt += 1
        print(path)
    else:
        for i in range(1,n+1):
            if graph[v][i] and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                dfs(i)
                ch[i] = 0
                path.pop()


n,m = map(int,input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
ch = [0]*(n+1)
for _ in range(m):
    n1,n2 = map(int,input().split())

    graph[n1][n2] = 1

cnt = 0
path = []
path.append(1)
ch[1] = 1
dfs(1)

print(cnt)