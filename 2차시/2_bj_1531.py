import sys

n,m = input().split(' ')
n,m = int(n),int(m)

img = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    p = list(map(int, sys.stdin.readline().rstrip()))
    img[p[0]:p[2]]

