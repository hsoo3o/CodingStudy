n,m = map(int, input().split())
song = list(map(int, input().split()))

s = 1
e = sum(song)
cnt = 1
num = 0
Ma = max(song)

while s <= e:
    mid = (s+e) // 2

    for i in song:
        num += i
        if num > mid:
            cnt += 1
            num = i
    print(s,e,mid,cnt)
    if cnt <= m and mid >= Ma:
        e = mid - 1
        ans = mid
    else:
        s = mid + 1

    cnt = 1
    num = 0

print(ans)