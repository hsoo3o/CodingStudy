# Baekjoon 14503

from sys import stdin
from collections import deque
import sys
from itertools import permutations

N, M = list(map(int, stdin.readline().split())) 
r, c, d = list(map(int, stdin.readline().split()))  # d: 0-north / 1-east / 2-south / 3-west
ans = 0
rot_count = 0

robot_map = []
clean_map = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    robot_map.append(list(map(int, stdin.readline().split())))

# 1
def clean_up():
    global ans, rot_count
    clean_map[r][c] = True
    ans += 1
    rot_count = 0

clean_up()
while True:
    # 2-1
    if rot_count != 4:
        if d == 0:
            d = 3
            if c-1 >= 0:
                if robot_map[r][c-1] == 0 and not clean_map[r][c-1]:
                    c -= 1
                    clean_up()
                    continue
            rot_count += 1
            continue
        elif d == 1:
            d = 0
            if r-1 >= 0:
                if robot_map[r-1][c] == 0 and not clean_map[r-1][c]:
                    r -= 1
                    clean_up()
                    continue
            rot_count += 1
            continue
        elif d == 2:
            d = 1
            if c+1 < M:
                if robot_map[r][c+1] == 0 and not clean_map[r][c+1]:
                    c += 1
                    clean_up()
                    continue
            rot_count += 1
            continue
        elif d == 3:
            d = 2
            if r+1 < N:
                if robot_map[r+1][c] == 0 and not clean_map[r+1][c]:
                    r += 1
                    clean_up()
                    continue
            rot_count += 1
            continue
    else:
        rot_count = 0
        if d == 0:
            if r+1 < N:
                if robot_map[r+1][c] == 0:
                    r += 1
                    continue
        elif d == 1:
            if c-1 >= 0:
                if robot_map[r][c-1] == 0:
                    c -= 1
                    continue
        elif d == 2:
            if r-1 >= 0:
                if robot_map[r-1][c] == 0:
                    r -= 1
                    continue
        elif d == 3:
            if c+1 < M:
                if robot_map[r][c+1] == 0:
                    c += 1
                    continue
    
        break

print(ans)