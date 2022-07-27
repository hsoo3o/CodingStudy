import sys
from collections import deque
import math

sys.setrecursionlimit(10 ** 5) 
input = sys.stdin.readline

N,L,R = map(int,input().split())
p = []
for _ in range(N):
    p.append(list(map(int,input().split())))

date = 0

while True:
    v = 0
    ch = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            temp = []
            dq = deque()
            if ch[row][col] == 0:
                dq.append([row,col])
                temp.append([row,col])
                people = p[row][col]
                cnt = 1
                while dq:
                    now = dq.popleft()
                    rr = now[0]
                    cc = now[1]
                    ch[rr][cc] = 1
                    dc = [-1, 0, 1, 0]
                    dr = [0, 1, 0, -1]
                    for i in range(4):
                        new_r = rr + dr[i]
                        new_c = cc + dc[i]
                        if 0 <= new_r < N and 0 <= new_c < N:
                            if ch[new_r][new_c] == 0:
                                if L <= abs(p[rr][cc] - p[new_r][new_c]) <= R:
                                    v = 1
                                    dq.append([new_r,new_c])
                                    people += p[new_r][new_c]
                                    cnt += 1
                                    temp.append([new_r,new_c])
                    print("dq:",dq)
            print("temp:", temp)
            if cnt != 0 and temp != []:
                for pos in temp:
                    row = pos[0]
                    col = pos[1]
                    p[row][col] = people // cnt
    print("")
    for _ in p:
        print(_)
    if v == 1:
        date += 1
    else:
        break
print(date)

