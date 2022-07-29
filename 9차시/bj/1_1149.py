import sys
def find(v, sum_,color):
    global min_sum
    print(color)
    nowcolor = color
    if v == N:
        if sum_ < min_sum:
            min_sum = sum_
    else:
        for i in range(3):
            if color[v] != i:
                nowcolor[v+1] = i
                find(v+1,sum_ + house[v][i],nowcolor)


N = int(sys.stdin.readline())

house = []
for _ in range(N):
    house.append(list(map(int,sys.stdin.readline().split())))
ans = 0
color = [-1 for _ in range(N+1)]
min_sum = 21470000000
find(0,0,color)
print(min_sum)