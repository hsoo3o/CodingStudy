N = int(input())
numbers = [i for i in range(1,N+1)]

def dfs(n):
    if n > N:
        return
    else:
        dfs(n+1)
        for i in range(1,n+1):
            print(i,end=' ')
        print("")
        dfs(n+1)
        

dfs(1)