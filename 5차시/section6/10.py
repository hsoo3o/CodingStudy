def dfs():
    q = set([1])
    ch[1] == 1

    while q:
        now = q.pop()
        for i in range(now + 1,n+1):
            q.add(i)
            print(now,' ',i)
                
        

n,m = map(int,input().split())

ch = [0]*(n+1)

dfs()