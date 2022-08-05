from collections import deque
import sys
def dfs(v,order):
    global min_sum,max_sum,sum_
    if v == opnum:
        order = iter(order)
        for i in range(1,n):
            o = next(order)
            if o == 0:
                sum_ += num[i]
            elif o == 1:
                sum_ -= num[i]
            elif o == 2:
                sum_ = sum_ * num[i]
            elif o == 3 and sum_ >= 0:
                sum_ = sum_ // num[i]
            elif o==3 and sum_ < 0:
                sum_ = -(-sum_//num[i])

        if sum_ < min_sum:
            min_sum = sum_
        if sum_ > max_sum:
            max_sum = sum_
        sum_ = num[0]
    else:
        for i in range(len(op)):
            if ch[i] == 0:
                ch[i] = 1
                dfs(v+1,order + [op[i]] )
                ch[i] = 0

n = int(sys.stdin.readline().rstrip())
num = list(map(int,sys.stdin.readline().split()))
math = list(map(int,sys.stdin.readline().split()))
sum_ = num[0]
op = []
for i in range(4):
    if math[i] != 0:
        [ op.append(i) for _ in range(math[i])]

opnum = sum(math)
ch = [0 for _ in range(opnum)]
max_sum = 0
min_sum = 21470000000
dfs(0,[])
print(max_sum)
print(min_sum)