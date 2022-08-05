from collections import deque
import sys



# T = int(sys.stdin.readline())

# for _ in range(T):
sticker = []
max_sum = 0
res = []
n = int(sys.stdin.readline())
for _ in range(2):
    sticker.append(list(map(int, sys.stdin.readline().rstrip().split())))

# dy = [[0 for _ in range(n)] for _ in range(2)]
q = deque([(0,0)])
sum_ = sticker[0][0]
while q:
    x,y = q.popleft()
    try:
        if x == 0:
            a = sticker[0][y+2]+sticker[1][y+1]
            b = sticker[1][y+2]
            if  a >= b:
                sum_ += a
                q.append((0,y+2))
            else:
                sum_ += b
                q.append((1,y+2))
        elif x == 1:
            sum += sticker[0][y+1]
            q.append((0,y+1))
    except:
        break


print(sum_)
    