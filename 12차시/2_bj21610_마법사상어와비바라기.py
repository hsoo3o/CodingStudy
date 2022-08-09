import sys
input = sys.stdin.readline
N,M = map(int,input().split())
baskets = [list(map(int,input().split())) for _ in range(N)]
cloud = [[0 for _ in range(N)] for _ in range(N)]

# 다음부터는
# dx = [0, -1, -1, -1, 0, 1, 1, 1]
# dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 형태로 구현하기
def direction(d):
    if d == 1:
        dr = 0
        dc = -1
    elif d == 2:
        dr = -1
        dc = -1
    elif d == 3:
        dr = -1
        dc = 0
    elif d == 4:
        dr = -1
        dc = 1
    elif d == 5:
        dr = 0
        dc = 1
    elif d == 6:
        dr = 1
        dc = 1
    elif d == 7:
        dr = 1
        dc = 0
    elif d == 8:
        dr = 1
        dc = -1
    return dr,dc

def move(r,c,nr,nc,s):
    global N
    # cnt = s // N
    r = (r + nr*s) % N
    c = (c + nc*s) % N

    return r,c

cloud[N-1][0] = 1
cloud[N-1][1] = 1
cloud[N-2][0] = 1
cloud[N-2][1] = 1


dgs_r = [1,1,-1,-1]
dgs_c = [1,-1,1,-1]


for i in range(1,M+1):
    d,s = map(int,input().split())
    nr,nc = direction(d)
    rained_area = []
    new_cloud = []

    # 1. 구름 이동
    for r in range(N):
        for c in range(N):
            if cloud[r][c] != 0:
                nnr,nnc = move(r,c,nr,nc,s)
                new_cloud.append((nnr,nnc)) # 처음에 new_cloud 따로 안만들고 한번에 해결하려해서 애먹음
    # 2. 비 내려서 바구니 물 증가
    for r,c in new_cloud:
        baskets[r][c] += 1

    # 3. 구름 모두 사라짐
    cloud = [[0 for _ in range(N)] for _ in range(N)]
    # 4. 물 복사 마법 시전
    for r,c in new_cloud:
        for j in range(4):
            nr = r + dgs_r[j]
            nc = c + dgs_c[j]
            if 0 <= nr < N and 0 <= nc < N and baskets[nr][nc] != 0:
                baskets[r][c] += 1
    # 5. 바구니 저장된 물의 양 2 이상인 모든 칸에 구름 생기고 물의 양 감소, 단 구름 생기는 칸은 3에서 사라진 칸 X
    for r in range(N):
        for c in range(N):
            if (r,c) not in new_cloud and baskets[r][c] >= 2:
                cloud[r][c] = 1
                baskets[r][c] -= 2

ans = 0

for r in range(N):
    for c in range(N):
        ans += baskets[r][c]

print(ans)

    

