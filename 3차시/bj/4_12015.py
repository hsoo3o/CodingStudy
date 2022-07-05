import sys
from collections import deque
n = int(input())

num = list(map(int, sys.stdin.readline().split(' ')))

sortnum = sorted(num)
ans = 0
mans = 0
res = []
p = 0
i = 0
lastindex = 0
for i in num:
    index = sortnum.index(i)

    res.append(index+p)
    sortnum[index] = 0
    
print(res)


for i in range(n-1):
    if res[i] > res[i+1] and ans >= mans:
        mans = ans
        ans = 0
    else:
        ans += 1
print(mans)
    

