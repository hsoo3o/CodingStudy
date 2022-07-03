N,M = list(map(int,input().split()))

n = list(map(int,input().split()))
n.sort()

s = 0
e = N-1
while s <= e:
    mid = (s+e) // 2
    if n[mid] == M:
        print(mid+1)
        break
    elif n[mid] > M:
        e = mid -1
    else:
        s = mid +1
    

