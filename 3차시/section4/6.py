N = int(input())
people = [list(map(int,input().split(' '))) for _ in range(N)]

people.sort(key=lambda x: x[0])
ans = 0

for i in range(N):
    w = people[i][1]
    cnt = 0
    for p in range(i,N):
        if people[p][1] < w:
            cnt += 1
    if cnt == N-i-1:
        ans += 1

print(ans)
