# Baekjoon 15686

from sys import stdin
from itertools import combinations

dx = [0,0,-1,1]
dy = [-1,1,0,0]
N, M = map(int, stdin.readline().rstrip().split(' '))
chicken_town = []
chicken_pos = []
house_pos = []
ans = 1e12
for i in range(N):
  line = list(map(int, stdin.readline().rstrip().split(' ')))
  chicken_town.append(line)
  for j in range(N):
    if line[j] == 2:
      chicken_pos.append([i,j])
    elif line[j] == 1:
      house_pos.append([i,j])

pos_combi = list(combinations(chicken_pos, M))

for pos in pos_combi:
  distance = 0
  for h_p in house_pos:
    dis = []
    for p in pos:
        dis.append(abs(h_p[0]-p[0]) + abs(h_p[1]-p[1]))
    distance += min(dis)
  ans = distance if distance < ans else ans
print(ans)