import sys

C,N = map(int,input().split())
weights = []
for i in range(N):
    weights.append(int(input()))
weights.sort()
total_weight = sum(weights)
weight_sum = []

def dfs(L,sum):
    if sum > C:
        return
    if L == N:
        weight_sum.append(sum)
    else:
        dfs(L+1,sum+weights[L])
        dfs(L+1,sum)
        

dfs(0,0)
print(max(weight_sum))
