import sys


n,k = map(int,sys.stdin.readline().split())

dy = [0 for _ in range(k+1)]

weight = []
value = []
for _ in range(n):
    w,v = map(int, sys.stdin.readline().split())
    weight.append(w)
    value.append(v)


    

print(dy)

