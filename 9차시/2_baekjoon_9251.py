# Baekjoon 9251

from sys import stdin
from collections import deque
import copy

ans = 0
string_a = stdin.readline().rstrip()
string_b = stdin.readline().rstrip()

LCS = [[0 for _ in range(len(string_b)+1)] for _ in range(len(string_a)+1)]
for i in range(len(string_a)):
    for j in range(len(string_b)):
        if string_a[i] == string_b[j]:
            LCS[i+1][j+1] = LCS[i][j] + 1
        else:
            LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])

for i in range(len(string_a)+1):
    ans = max(ans, max(LCS[i]))
print(ans)