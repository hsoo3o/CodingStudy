n,m = map(int,input().split())
d = [(idx,val) for idx,val in enumerate(list(map(int, input().split())))]


cnt = 0
while True:
    d1 = d.pop(0)
    if any(d[cnt][1] <= left for left in d):
        d.append(d1)
    else:
        cnt += 1
        if d1[0] == m:
            break
print(cnt)
