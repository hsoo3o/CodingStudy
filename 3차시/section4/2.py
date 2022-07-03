import sys
import time
k,n = map(int,input().split())

ran = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(k)]
s = 1
e = max(ran)[0]
cnt = 0
ans = 0
while s<=e:
    mid = (s+e)//2

    for i in ran:
        cnt += i[0] // mid
    
    if cnt >= n:
        ans = mid
        s = mid + 1
    elif cnt < n:
        e = mid - 1
    cnt = 0
print(ans)




        



