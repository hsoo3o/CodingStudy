import sys
input = sys.stdin.readline
K = int(input())
weights = list(map(int,input().split()))
possible = set()
max = sum(weights)
def dfs(L,sum):
    if L == K:
        if 0 < sum <= max:
            possible.add(sum)
        return
    dfs(L+1,sum+weights[L])
    dfs(L+1,sum-weights[L])
    dfs(L+1,sum)
        

dfs(0,0)
print(max-len(possible))

