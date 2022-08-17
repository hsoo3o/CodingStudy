# Baekjoon 14891

from sys import stdin
# N:0 / S:1
# Clockwise : -1
# Counter-clockwise : +1
ans = 0
gear1 = stdin.readline().rstrip()
gear2 = stdin.readline().rstrip()
gear3 = stdin.readline().rstrip()
gear4 = stdin.readline().rstrip()
N = int(stdin.readline().rstrip())
index1 = 2
index2 = [6,2] # 2-1, 2-3
index3 = [6,2] # 3-2, 3-4
index4 = 6

for i in range(N):
  gear_num, direction = list(map(int, stdin.readline().rstrip().split(' ')))
  # Default: Counter-Clockwise
  dir1 = 0
  dir2 = 0
  dir3 = 0
  dir4 = 0

  if gear_num == 1:
    dir1 = 1
    if gear1[index1] != gear2[index2[0]]:
      dir2 = -1
      if gear2[index2[1]] != gear3[index3[0]]:
        dir3 = 1
        if gear3[index3[1]] != gear4[index4]:
          dir4 = -1

  elif gear_num == 2:
    dir2 = 1
    if gear1[index1] != gear2[index2[0]]:
      dir1 = -1
    if gear2[index2[1]] != gear3[index3[0]]:
      dir3 = -1
      if gear3[index3[1]] != gear4[index4]:
        dir4 = 1

  elif gear_num == 3:
    dir3 = 1
    if gear2[index2[1]] != gear3[index3[0]]:
      dir2 = -1
      if gear1[index1] != gear2[index2[0]]:
        dir1 = 1
    if gear3[index3[1]] != gear4[index4]:
      dir4 = -1

  elif gear_num == 4:
    dir4 = 1
    if gear3[index3[1]] != gear4[index4]:
      dir3 = -1
      if gear2[index2[1]] != gear3[index3[0]]:
        dir2 = 1
        if gear1[index1] != gear2[index2[0]]:
          dir1 = -1

  if direction == 1:
    dir1 *= -1
    dir2 *= -1
    dir3 *= -1
    dir4 *= -1

  index1 = (index1 + dir1) % 8
  index2[0] = (index2[0] + dir2) % 8
  index2[1] = (index2[1] + dir2) % 8
  index3[0] = (index3[0] + dir3) % 8
  index3[1] = (index3[1] + dir3) % 8
  index4 = (index4 + dir4) % 8

if gear1[(index1-2)%8] == '1':
  ans += 1
if gear2[(index2[1]-2)%8] == '1':
  ans += 2
if gear3[(index3[1]-2)%8] == '1':
  ans += 4
if gear4[(index4-6)%8] == '1':
  ans += 8
print(ans)