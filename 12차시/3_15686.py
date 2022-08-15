from itertools import combinations
import sys


N,M = map(int, sys.stdin.readline().split())
house = {}
chicken = []
len_chicken = 0
ans = 0
min_ans = 2147000000
for i in range(N):
    city = list( map(int, sys.stdin.readline().split()))
    for j in range(N):
        if city[j] == 1:
            house[(i+1,j+1)] = []
        elif city[j] == 2:
            chicken.append([i+1,j+1])
            len_chicken += 1
chicken_list = [i for i in range(len_chicken)]
left_chicken = combinations(chicken_list,M)

for r1,c1 in house.keys():
    for r2,c2 in chicken:
        dist = abs(r1-r2)+abs(c1-c2)
        house[(r1,c1)].append(dist)
for lefts in left_chicken:
    for h in house:
        min_ = 2147000000
        distances = house[h]
        for i in lefts:
            if distances[i] < min_:
                min_ = distances[i]
        ans += min_
    
    if ans < min_ans:
        min_ans = ans
    ans = 0


print(min_ans)



