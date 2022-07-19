# 무방향 그래프, 방향 그래프를 인접행렬로 표현해보자
# 인접행렬은 "행->열" 번호로 이동한다고 생각하자

# 무방향 그래프
N,M = map(int,input().split()) # N : 노드 번호, M : 간선의 개수
g = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a,b,c = map(int,input().split())
    g[a][b] = c

for i in range(1,N+1):
    for j in range(1,N+1):
        print(g[i][j], end=' ')
    print()