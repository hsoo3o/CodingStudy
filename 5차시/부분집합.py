# dfs 하려면 상태트리를 잘 구성하면 됨
N = int(input())
ch = [0]*(N+1)

sets = []
def dfs(v):
    if v > N:
        for i in range(1,N+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
        return
    else:
        ch[v] = 1
        dfs(v+1)
        ch[v] = 0
        dfs(v+1)
dfs(1)
