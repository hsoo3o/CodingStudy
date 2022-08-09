# Baekjoon 14501

from sys import stdin
from collections import deque
import sys

N = int(stdin.readline())
T, P = [], []
dp = [0 for _ in range(N)]
for i in range(N):
    Ti, Pi = list(map(int, stdin.readline().split()))
    T.append(Ti)
    P.append(Pi)

for i in range(N):
    maximum = P[i]
    if i + T[i] <= N:
        for j in range(i):
            if j + T[j] <= i:
                maximum = dp[j] + P[i] if dp[j] + P[i] > maximum else maximum
        dp[i] = maximum
print(max(dp))