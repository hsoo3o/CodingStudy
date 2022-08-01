# Baekjoon 9465

from sys import stdin

T = int(stdin.readline())
for t in range(T):
    N = int(stdin.readline())
    row_1 = list(map(int, stdin.readline().split()))
    row_2 = list(map(int, stdin.readline().split()))
    maximum_scores = []
    # First
    maximum_scores.append([row_1[0], row_2[0]])
    if N == 1:
        print(max(maximum_scores[-1][0], maximum_scores[-1][1]))
        continue
    # Second
    maximum_scores.append([row_2[0] + row_1[1], row_1[0] + row_2[1]])
    for i in range(2, N):
        maximum_scores.append([max(maximum_scores[i-2][1], maximum_scores[i-1][1]) + row_1[i], max(maximum_scores[i-2][0], maximum_scores[i-1][0]) + row_2[i]])

    print(max(maximum_scores[-1][0], maximum_scores[-1][1]))