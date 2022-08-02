import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    line = []
    line.append(list(map(int,input().split())))
    line.append(list(map(int,input().split())))
    for c in range(1,n):
        if c == 1:
            line[0][c] += line[1][c-1]
            line[1][c] += line[0][c-1]
        else:
            line[0][c] += max(line[1][c-1], line[1][c-2])
            line[1][c] += max(line[0][c-1], line[0][c-2])
    print(max(line[0][-1],line[1][-1]))
