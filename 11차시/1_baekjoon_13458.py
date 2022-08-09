# Baekjoon 11048

from sys import stdin

N, M = list(map(int, stdin.readline().split()))
maximum_candy_map = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    candys = list(map(int, stdin.readline().split()))
    if i == 0:
        maximum_candy_map[0][0] = candys[0]
        for j in range(1, M):
            maximum_candy_map[i][j] = candys[j] + maximum_candy_map[i][j-1]
    else:
        maximum_candy_map[i][0] = maximum_candy_map[i-1][0] + candys[0]
        for j in range(1, M):
            maximum_candy_map[i][j] = max(maximum_candy_map[i][j-1], maximum_candy_map[i-1][j]) + candys[j]

print(maximum_candy_map[-1][-1])