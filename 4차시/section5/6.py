n,m = map(int,input().split())
d = list(map(int, input().split()))
q = [i for i in range(n)]
print(q)
cnt = 0
while True:
    p = q.pop(0)
    d1 = d.pop(0)
    print(p,q,d,cnt)
    if any(d[p-cnt] < left for left in d):
        q.append(p)
        d.append(d1)
    else:
        if p != m:
            cnt += 1
        else:
            cnt += 1
            break
    print(cnt,d)
print(cnt)
