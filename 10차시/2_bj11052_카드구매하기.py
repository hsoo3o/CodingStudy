import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int,input().split()))
card.insert(0,0)
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + card[j])
print(dp[-1])
