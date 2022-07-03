n,m = map(int, input().split())

weight = list(map(int,input().split()))
weight.sort(reverse=True)

ans = 0
num = 0
s = 0
e = n-1
while s <= e:
    up = weight[s] + weight[e]
    if up > m:
        s = s+1
        num += 1
    else:
        s += 1
        e -= 1
        num += 2
    
    ans += 1
    if num == n:
        break
    
print(ans)

