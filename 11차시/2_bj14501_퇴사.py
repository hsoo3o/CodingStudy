# dp
N = int(input())
table = []
for i in range(N):
    table.append(list(map(int, input().split())))
dp = [0 for _ in range(N+1)]

for j in range(len(table)-1, -1, -1):
    if table[j][0] > (N-j):
#         print("if 1", N-j)
#         print(table[j][0])
        dp[j] = dp[j+1]
    else:
#         print("if 2", N-j)
        dp[j] = max(dp[j+1] ,table[j][1] + dp[j+table[j][0]])
        
print(max(dp))

# dfs
N = int(input())
table = [list(map(int,input().split())) for _ in range(N)]
ans = 0

def dfs(L,p):
    global ans
    if L > N:
        return
    if L == N:
        if p > ans:
            ans = p
        return
    else:
        dfs(L+table[L][0],p+table[L][1])
        dfs(L+1,p)

dfs(0,0)

print(ans)