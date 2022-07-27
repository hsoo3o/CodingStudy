# 큐 자료구조를 사용, 출발점에서 어떤 거리로 가는 가장 짧은 거리가 무엇인지 탐색할 때 사용


import sys
from collections import deque

input = sys.stdin.readline

max = 10000
ch = [0] * (max+1)
dis = [0] * (max+1)
n,m = map(int,input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ: # BFS는 비어있으면 멈춤
    now = dQ.popleft()
    if now == m:
        break
    for next in (now-1, now+1, now+5):
        if 0 < next<= 10000:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now]+1                
print(dis[m])
