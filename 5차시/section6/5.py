
def DFS(L,sum_):
    global max_sum 
    if L == n:
        if sum_ > max_sum:
            max_sum = sum_
    else:
        DFS(L+1,sum_+dog[L])
        DFS(L+1,sum_)

max_sum = 0
c,n = map(int,input().split())
dog = list(int(input()) for _ in range(n))
DFS(0,0)
print(max_sum)
