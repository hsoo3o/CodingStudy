n = int(input())

line = list(map(int,input().split()))

dy = [0] * (n+1)
line.insert(0,0)
dy[1] = 1
res = 0
for i in range(2,n+1):
    max_ = 0
    for j in range(i):
        if line[j] < line[i] and dy[j] > max_:
            max_ = dy[j]
    dy[j] = max_+1
    if dy[j] > res:
        res = dy[j]

print(res)