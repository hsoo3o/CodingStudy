import sys
n,c = map(int,input().split())

w = []
for _ in range(n):
    w.append(int(sys.stdin.readline()))

w.sort()
s = 1
e = w[-1]-w[0]
ans = 0
while s<=e:
    mid = (s+e)// 2
    cnt = 1
    h = w[0]
    for i in range(1,n):
        if w[i] - h >= mid:
            cnt += 1
            h = w[i]
    if cnt >= c:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1 
print(ans)