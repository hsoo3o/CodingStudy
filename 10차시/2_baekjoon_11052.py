# Baekjoon 11052

from sys import stdin

N = int(stdin.readline())
maximum_price = [0 for _ in range(N)]
cards = list(map(int, stdin.readline().split()))
maximum_price[0] = cards[0]
for i in range(N):
    best_price = 0
    for j in range((i+1)//2):
        best_price = max(best_price, maximum_price[i-1-j] + maximum_price[j])
    maximum_price[i] = max(best_price, cards[i])

print(maximum_price[-1])