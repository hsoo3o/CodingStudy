n,c = map(int,input().split())
horse = []

for _ in range(n):
    horse.append(int(input()))

horse.sort()
s = 1
e = horse[n-1]
h = horse[0]
cnt = 1
answ = 0
while s<=e:
    mid = (s+e)//2

    for i in range(1,n):
        if horse[i] - h >= mid:
            cnt += 1
            h = horse[i]

    if cnt >= c:
        answ = mid
        s = mid +1
    else:
        e = mid -1
    
    cnt = 1
    h = horse[0]
print(answ)