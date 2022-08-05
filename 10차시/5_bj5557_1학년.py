import sys
import math
input = sys.stdin.readline

# n = int(input())
# numbers = list(map(int,input().split()))

# zeros = 0

# while 0 in numbers:
#     numbers.pop(numbers.index(0))
#     zeros += 1

# cnt = 0
# tmp = 0
# def dfs(numbers,L,tmp):
#     global cnt
#     if tmp > 20 or tmp < 0:
#         return
#     if L == n-1-zeros and tmp == numbers[-1]:
#         cnt += 1
#         return
#     if L > n-1-zeros:
#         return
#     else:
#         tmp += numbers[L]
#         dfs(numbers,L+1,tmp)
#         tmp -= 2*numbers[L]
#         dfs(numbers,L+1,tmp)

# dfs(numbers,0,tmp)

# print(cnt*(zeros+1))

N = int(input()) 
numbers = list(map(int, input().split()))  

dp = [[0 for _ in range(21)] for _ in range(N-1)]
dp[0][numbers[0]] = 1

for r in range(1, N - 1):
    for c in range(21):
        if dp[r-1][c] != 0:
            now = c
            next = numbers[r]

            plus = now + next
            if 0 <= plus <= 20:
                dp[r][plus] += dp[r-1][now]

            minus = now - next
            if 0 <= minus <= 20:
                dp[r][minus] += dp[r-1][now]

print(dp[-1][numbers[-1]])