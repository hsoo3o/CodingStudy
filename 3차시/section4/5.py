n = int(input())
room = [list(map(int,input().split(' '))) for _ in range(n)]

room.sort(key=lambda x: x[1])
end = room[0][1]
cnt = 1
for i in range(1,n):
    if room[i][0] >= end:
        end = room[i][1]
        cnt += 1
    else:
        continue 

print(cnt)