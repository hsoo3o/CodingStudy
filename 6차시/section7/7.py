
from collections import deque



s,e = map(int,input().split())
dist = [0] * (10001)
ch = [0] * (10001)
ch[s] = 1


q = deque([s])
while q:
    now = q.popleft()
    ch[now] = 1
    if now == e:
        print(dist[now])
        break
    else:
        for next in (now-1,now+1,now+5):
            if 0< next < 10000:
                if ch[next] == 0:
                    q.append(next)
                    ch[next] = 1
                    dist[next] = dist[now] +1