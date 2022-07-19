n = int(input()) # 전체 사람
p1, p2 = map(int,input().split()) # 촌수 계산해야하는 서로 다른 두 사람 번호
m = int(input()) # 부모 자식들 간의 관계의 개수

# relations = [[0]*(n+1) for _ in range(n+1)]
relations = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = []

for i in range(m):
    x,y = map(int,input().split())
    relations[x].append(y)
    relations[y].append(x)

def dfs(L,cnt):
    cnt += 1
    visited[L] = True
    if L == p2:
        ans.append(cnt)
    for i in relations[L]:
        if not visited[i]:
            dfs(i,cnt)
dfs(p1,0)
if len(ans) == 0:
    print(-1)
else:
    print(ans[0]-1)