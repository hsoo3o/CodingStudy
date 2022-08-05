import sys


n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
max_sum = 0
dy = [0]*(n+1)
card.insert(0,0)
for i in range(1,n+1):
    for j in range(i,n+1):
        dy[j] = max(dy[j], dy[j-i]+card[i])

print(dy[n])