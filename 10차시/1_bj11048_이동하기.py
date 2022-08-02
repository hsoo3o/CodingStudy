import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

for r in range(N):
    for c in range(M):
        if r == 0 and c ==0:
            pass
        elif r == 0 and c > 0:
            graph[r][c] += graph[r][c-1]
        elif r > 0 and c == 0:
            graph[r][c] += graph[r-1][c]
        else:
            graph[r][c] += max(graph[r-1][c-1],graph[r-1][c], graph[r][c-1])

print(graph[-1][-1])

