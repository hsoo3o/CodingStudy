# Top-donw : 재귀,메모이제이션
# 경우의 수 : 마지막을 1로 자르는 경우의 수, 2로 자르는 경우의 수 로 나눈 뒤 나머지 토막에 대해 재귀 반복

n = int(input())

dp = [[] for _ in range(n+1)]
dp[1] = 1
dp[2] = 2


def dfs(N):
    global dp
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        if dp[N-1] != []:
            tmp1 = dp[N-1]
        else:
            dp[N-1] = dfs(N-1)
            tmp1 = dfs(N-1)
        if dp[N-2] != []:
            tmp2 = dp[N-2]
        else:
            dp[N-2] = dfs(N-2)
            tmp2 = dp[N-2]            
        return tmp1 + tmp2
print(dfs(7))


