from collections import deque
import sys
gear = []
for _ in range(4):
    gear.append(list(sys.stdin.readline().rstrip()))

k = int(sys.stdin.readline().rstrip())

for _ in range(k):
    ch = [0,0,0,0]
    q = deque()
    direction = [0,0,0,0]
    num,dir =  map(int, sys.stdin.readline().split())
    num = num -1

    direction[num] = dir
    ch[num] = 1
    q.append(num)
    while q:
        num0 = q.popleft()
        num1 = num0 - 1
        num2 = num0 + 1
        if num1 >= 0 and ch[num1] == 0:
            ch[num1] = 1
            if gear[num1][2] != gear[num0][6]:
                direction[num1] = -direction[num0]
                q.append(num1)
        if num2 < 4 and ch[num2] == 0:
            ch[num2] = 1
            if gear[num0][2] != gear[num2][6]:
                direction[num2] = -direction[num0]
                q.append(num2)
    for i in range(4):
        if direction[i] == 1:
            gear[i] = [gear[i][-1]] + gear[i][0:7]
        elif direction[i] == -1:
            gear[i] = gear[i][1:] + [gear[i][0]]

ans = 0
score = [1,2,4,8]
for i in range(4):
    if gear[i][0] == '1':
        ans += score[i]
print(ans)


