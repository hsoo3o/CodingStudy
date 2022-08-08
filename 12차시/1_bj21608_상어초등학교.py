from collections import deque

N = int(input())
students = [list(map(int,input().split())) for _ in range(N**2)]
sits = [[0]*N for _ in range(N)]

q = deque()

dr = [1,-1,0,0]
dc = [0,0,1,-1]

for i in range(N**2):

    # if i == 0:
    #     center = N//2
    #     student = students[i][0]
    #     sits[center][center] = student
    # else:
    student = students[i][0]
    favorites = students[i][1:]
    visited = [[0]*N for _ in range(N)]
    cand = []
    for x in range(N):
        for y in range(N):
            if sits[x][y] == 0:
                q.append([x,y])
                while q:
                    now = q.popleft()
                    r = now[0]
                    c = now[1]
                    cnt = 0
                    empty_cnt = 0
                    for j in range(4):
                        nr = r + dr[j]
                        nc = c + dc[j]
                        if 0 <= nr < N and 0 <= nc < N:
                            if sits[nr][nc] in favorites:
                                cnt += 1
                            elif sits[nr][nc] == 0:
                                empty_cnt += 1

                    cand.append([x,y,cnt,empty_cnt])
    cand.sort(key=lambda x: (x[2],x[3],-x[0],-x[1]),reverse=True)

    r = cand[0][0]
    c = cand[0][1]
    sits[r][c] = student

head = []
for i in range(N**2):
    head.append(students[i][0])
ans = 0
i = 0
for r in range(N):
    for c in range(N):
        favorites = students[head.index(sits[r][c])][1:]
        i += 1
        cnt = 0
        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]
            if 0 <= nr < N and 0 <= nc < N and sits[nr][nc] in favorites:
                cnt += 1
        if cnt == 0:
            pass
        elif cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
print(ans)
# for _ in sits:
#     print(_)


