# Baekjoon 14889

from sys import stdin
from collections import deque
import sys
from itertools import combinations

N = int(stdin.readline())

soccer = []
scores = []
ans = 1e12
for i in range(N):
    line = list(map(int, stdin.readline().split()))
    soccer.append(line)

combi = list(combinations(range(N), N//2))
for c_1 in combi:
    c_2 = []
    for i in range(N):
        if i not in c_1:
            c_2.append(i)
    capability_1 = 0
    capability_2 = 0
    for i in c_1:
        for j in c_1:
            capability_1 += soccer[i][j]
    for i in c_2:
        for j in c_2:
            capability_2 += soccer[i][j]

    ans = abs(capability_1-capability_2) if abs(capability_1-capability_2) < ans else ans
    if ans == 0:
        break

print(ans)
