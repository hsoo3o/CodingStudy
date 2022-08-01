n = int(input())

block = []

for _ in range(n):
    block.append(list(map(int,input().split())))

dy = [0] * (n)
block.sort(reverse=True)
dy[0] = block[0][1]
res = block[0][1]
for i in range(1,n):
    max_ = 0
    for j in range(i):
        if block[j][2] > block[i][2] and dy[j] > max_:
            max_ = dy[j]
    dy[i] = max_ + block[i][1]
    if dy[i] > res:
        res = dy[i]

print(res)

