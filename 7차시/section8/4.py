n = int(input())
num = list(map(int,input().split()))

num.insert(0,0)
dy = [0]*(n+1)
dy[1] = 1

for i in range(2,n+1):
    max_ = 0
    for j in range(i):
        if num[j] < num[i] and dy[j] > max_:
            max_ = dy[j]
    dy[i] = max_ + 1

print(max(dy))