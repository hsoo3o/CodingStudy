
n,m = map(int,input().split(' '))

q = [i for i in range(1,n+1)]
cnt = 1
while len(q) != 1:
    k = q.pop(0)
    if cnt == m:
        cnt = 1
    else:
        q.append(k)
        cnt += 1

print(q.pop())
