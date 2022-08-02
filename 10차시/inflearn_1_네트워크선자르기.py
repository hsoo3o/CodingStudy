# memoization
# Bottom up : 점화식을 잘 찾는 것이 중요!

n = int(input())

dy = [[] for _ in range(n)]
dy[0] = 1
dy[1] = 2

for i in range(2,n):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[-1])