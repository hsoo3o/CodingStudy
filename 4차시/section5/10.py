import heapq
h = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(h) == 0:
            print(-1)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h,n)

    