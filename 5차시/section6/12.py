

n,m = map(int,input().split())

graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    n1,n2,w = map(int,input().split())

    graph[n1-1][n2-1] = w

print(graph)