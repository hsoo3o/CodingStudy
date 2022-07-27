from operator import ne
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
# Tree = []
# for i in range(n):
#     Tree.append(list(map(int,input().split())))

# mid = n // 2
# cnt = n // 2
# apples = 0
# for i in range(n):
#     if i == 0 or i == n:
#         apples += Tree[i][cnt]
#     elif i > mid:
#         l += 1
#         r -= 1
#         apples += sum(Tree[i][l:r+1])
#     else:
#         l = cnt - i
#         r = cnt + i
#         apples += sum(Tree[i][l:r+1])
# print(apples)


## BFS,  BFS는 마름모로 커짐

Tree = []
for i in range(n):
    Tree.append(list(map(int,input().split())))

ch = [[0] * (n+1) for _ in range(n+1)]
apples = 0
dQ = deque()
dQ.append([n//2, n//2])
while dQ:
    now = dQ.popleft()
    if 0 in now or n in now:
        break
    for next in ([now[0]-1,now[1]],[now[0],now[1]+1],[now[0]+1,now[1]],[now[0],now[1]-1]):
        if ch[next[1]][next[0]] == 0:
            dQ.append(next)
            ch[next[1]][next[0]] = 1
            apples += Tree[next[1]][next[0]]
print(apples)