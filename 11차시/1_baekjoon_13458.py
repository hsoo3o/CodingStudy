# Baekjoon 13458

from sys import stdin
from collections import deque
import sys

N = int(stdin.readline())
candidates = list(map(int, stdin.readline().split()))
B, C = list(map(int, stdin.readline().split()))

ans = 0
for i in range(N):
    people = candidates[i]
    people = 0 if B > people else people - B
    ans += (people+C-1) // C + 1
print(ans)