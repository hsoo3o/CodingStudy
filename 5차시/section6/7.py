
def BFS(v,sum_):
    global min_num
    if v>=min_num:
        return
    if sum_ > m:
        return
    if sum_ == m:
        if min_num > v:
            min_num = v
    else:
        for i in coin:
            BFS(v+1, sum_ + i)

min_num = 2147000000
n = int(input())
coin = list(map(int,input().split()))
coin.sort(reverse=True)
m = int(input())
BFS(0,0)
print(min_num)

