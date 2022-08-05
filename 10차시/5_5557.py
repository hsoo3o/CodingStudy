import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().split()))
ans = 0

dy = [0 for _ in range(21)]

for i in range(n):
    for j in range(20,pt[i]-1,-1):
        dy[j] = max(dy[j], dy[j-pt[i]]+pv[i])


print(dy[m])
